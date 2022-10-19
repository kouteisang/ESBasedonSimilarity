# @Author : Cheng Huang
# @Time   : 14:10 2022/10/19
# @File   : distmult_embedding.py

import os
from pykeen.triples import TriplesFactory
from pykeen.losses import MarginRankingLoss
from pykeen.pipeline import pipeline
from pykeen.optimizers import Adam
from pykeen.evaluation import RankBasedEvaluator
from pykeen.models import DistMult
import torch
from pykeen.models.predict import get_tail_prediction_df



def get_embedding(path, training, testing, validation):

    # grid search to find the best hyper-parameter
    dbmodel = None
    if "dbpedia" in path:
        dbmodel = pipeline(
            training=training,
            testing=testing,
            validation=validation,
            training_loop='sLCWA',
            negative_sampler='basic',
            loss=MarginRankingLoss,
            loss_kwargs = dict(margin=1),
            model_kwargs = dict(
                # scoring_fct_norm = 2,
                embedding_dim=100),
            optimizer=Adam,
            optimizer_kwargs=dict(lr=0.001),
            stopper="early",
            model=DistMult,
            epochs=300
        )
        dbmodel.save_to_directory('model_distmult_dbpedia/dbpedia_distmult_model')

    lmmodel = None
    if "lmdb" in path:
        lmmodel = pipeline(
            training=training,
            testing=testing,
            validation=validation,
            training_loop='sLCWA',
            negative_sampler='basic',
            loss=MarginRankingLoss,
            loss_kwargs = dict(margin=1),
            model_kwargs = dict(
                embedding_dim=100),
            optimizer=Adam,
            optimizer_kwargs=dict(lr=0.01),
            stopper="early",
            model=DistMult,
            epochs=300
        )
        lmmodel.save_to_directory('model_distmult_lmdb/lmdb_distmult_model')

# This method is to evaluate the model
# using MRR and hits@10
def evluate_model(path, training, testing, validation):
    evaluator = RankBasedEvaluator()
    model = None
    if "dbpedia" in path:
        model = torch.load(os.path.join(os.getcwd(),"model_distmult_dbpedia/dbpedia_distmult_model/trained_model.pkl"))
    else:
        model = torch.load(os.path.join(os.getcwd(),"model_distmult_lmdb/lmdb_distmult_model/trained_model.pkl"))
    result = evaluator.evaluate(
        model=model,
        mapped_triples=testing.mapped_triples,
        batch_size=1024,
        additional_filter_triples=[
            training.mapped_triples,
            validation.mapped_triples
        ]
    )
    print("MRR = ", result.get_metric("meanreciprocalrank"))
    print("hits@10 = ", result.get_metric("hits@10"))



def choose(path):
    tf = TriplesFactory.from_path(path)
    # split the data into training set, testing set, validation set
    training, testing, validation = tf.split([.85, .075, .075])
    # train the model to get the embedding
    get_embedding(path, training, testing, validation)
    # evluate the model
    evluate_model(path, training, testing, validation)

if __name__ == '__main__':
    root = os.path.abspath(os.path.dirname(os.getcwd()))
    db_path = os.path.join(root, "data_analysis", "dbpedia", "dbpedia_all.txt")
    lm_path = os.path.join(root, "data_analysis", "lmdb", "lmdb_all.txt")

    choose(lm_path)




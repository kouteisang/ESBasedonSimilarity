# @Author : Cheng Huang
# @Time   : 15:11 2022/9/12
# @File   : fuzzy_k_means.py
import copy
import random
import numpy as np

# This function is for test FCM class
def normalise_U(U):
    """
    在聚类结束时使U模糊化。每个样本的隶属度最大的为1，其余为0
    """
    for i in range(0, len(U)):
        maximum = max(U[i])
        for j in range(0, len(U[0])):
            if U[i][j] != maximum:
                U[i][j] = 0
            else:
                U[i][j] = 1
    return U

# This function is for test FCM class
def de_randomise_data(data, order):
    """
    此函数将返回数据的原始顺序，将randomise_data()返回的order列表作为参数
    """
    new_data = [[] for i in range(0, len(data))]
    for index in range(len(order)):
        new_data[order[index]] = data[index]
    return new_data

# This function is for test FCM class
def checker_iris(final_location):
    """
    compare with the tree label
    """
    right = 0.0
    for k in range(0, 3):
        checker = [0, 0, 0]
        for i in range(0, 50):
            for j in range(0, len(final_location[0])):
                if final_location[i + (50 * k)][j] == 1:  # i+(50*k)表示 j表示第j类
                    checker[j] += 1  # checker分别统计每一类分类正确的个数
        right += max(checker)  # 累加分类正确的个数
    print('分类正确的个数是:', right)
    answer = right / 150 * 100
    return "准确率：" + str(answer) + "%"

# This function is for test FCM class
def randomize_data(data):
    """
    该功能将数据随机化，并保持随机化顺序的记录
    """
    order = list(range(0, len(data)))
    random.shuffle(order)
    new_data = [[] for i in range(0, len(data))]
    for index in range(0, len(order)):
        new_data[index] = data[order[index]]
    return new_data, order

# This function is for test FCM class
def import_data_format_iris(file):
    """
    file这里是输入文件的路径，如iris.txt.
    格式化数据，前四列为data，最后一列为类标号（有0，1，2三类）
    如果是你自己的data，就不需要执行此段函数了。
    """
    data = []
    cluster_location = []
    with open(str(file), 'r') as f:
        for line in f:
            current = line.strip().split(",")  # 对每一行以逗号为分割，返回一个list
            current_dummy = []
            for j in range(0, len(current) - 1):
                current_dummy.append(float(current[j]))  # current_dummy存放data

            # 下面注这段话提供了一个范例：若类标号不是0，1，2之类数字时该怎么给数据集
            j += 1
            if current[j] == "Iris-setosa\n":
                cluster_location.append(0)
            elif current[j] == "Iris-versicolor\n":
                cluster_location.append(1)
            else:
                cluster_location.append(2)
            data.append(current_dummy)
    print("加载数据完毕")
    return data


class FCM:
    '''
    This class is the implementation of FCM algorithm(a.k.a soft clustering algorithm)

    Args:
        data: Data need to be clustered
        cluster_number: The number of cluster we want to get
        m: m is the fuzzy parameter, the bigger the m, the fuzzy the result we get
        threshold: stop criteria

    Returns:
        The soft clustering result
    '''
    def __init__(self, data, cluster_number, m, threshold):
        self.data = np.array(data)
        self.cluster_number = cluster_number
        self.m = m
        self.U = self.initialize_U()
        self.row = len(self.data)
        self.col = len(self.data[0])
        self.threshold = threshold

    # This function is to random generate the U matrix
    def initialize_U(self):
        U = np.zeros((len(self.data), self.cluster_number))
        M = 10000.0

        for i in range(len(data)):
            temp = []
            for j in range(self.cluster_number):
                temp.append(random.randint(1, int(M)))
            U[i] = [val/sum(temp) for val in temp]

        return U

    # this function is to get the final result
    def forward(self):
        return self.update_u()

    # return the centroidfor each cluster
    def calculate_centroid(self):
        row = self.row
        col = self.col
        centroid = np.zeros((self.cluster_number, col))

        for j in range(self.cluster_number):
            nu = np.zeros(col, dtype=float)
            de = 0.0
            for i in range(row):
                de = de + (self.U[i][j]**self.m)
                nu = nu + ((self.U[i][j]**self.m) * np.array(self.data[i]))
            centroid[j] = nu/de

        return centroid

    # stop criteria old_u - new_u must smaller than the threshold
    def stop_criteria(self, old, new):
        for i in range(len(data)):
            for j in range(self.cluster_number):
                if abs(old[i][j] - new[i][j]) > self.threshold:
                    return False
        return True

    # update the U matrix
    # U matrix represent the probability distribution for each data point to different cluster
    def update_u(self):
        while True:
            dist = np.zeros((self.row, self.cluster_number), dtype=float)
            centroid = self.calculate_centroid()
            for i in range(self.row):
                for j in range(self.cluster_number):
                    # here we use the L2 norm
                    dist[i][j] = np.linalg.norm(self.data[i]-centroid[j])

            old_U = copy.deepcopy(self.U)
            for i in range(self.row):
                for k in range(self.cluster_number):
                    sum = 0.0
                    for j in range(self.cluster_number):
                        sum = sum + (dist[i][k]/dist[i][j])**(2/(self.m-1))
                    self.U[i][k] = 1.0/sum

            if self.stop_criteria(old_U, self.U) == True:
                self.U = normalise_U(self.U)
                return self.U


if __name__ == '__main__':
    data = import_data_format_iris("iris.txt")
    # 随机化数据
    data, order = randomize_data(data)
    # print_matrix(data)
    fcm = FCM(data, 3, 4, 0.001)
    final_location = de_randomise_data(fcm.forward(), order)
    print(checker_iris(final_location))
import cmath as cm
import numpy as np

class BasicCal():
    def add(self):
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))

        return f"Kết quả là: {a + b}"

    def sub(self):
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))

        return f"Kết quả là: {a - b}"

    def mul(self):
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))

        return f"Kết quả là: {a * b}"

    def div(self):
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))

        return f"Kết quả là: {a / b}"

    def _f(self,x,n,a):
        return x**n - a

    def _df(self,x,n):
        return n*x**(n-1)

    def root(self):
        a = float(input("Nhập số: "))
        n = int(input("nhập n:"))
        x = 0

        while True:
            x = np.random.randint(0,int(a))
            if x != 0:
                break

        for i in range(50):
            x = x - self._f(x,n,a)/self._df(x,n)

        return f"Căn bậc {n} của {a} là: {x}"


class Compare():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def compare(self):
        if self.a > self.b:
            print(f"{self.a} lớn hơn {self.b}")

        elif self.a < self.b:
            print(f"{self.a} bé hơn {self.b}")

        else:
            print(f"{self.a} bằng {self.b}")


class Geomertry():
    def Hcn(self,mess):
        a = float(input("Nhập cạnh thứ nhất: "))
        b = float(input("Nhập cạnh thứ hai: "))

        if mess == "Chu vi" or "chu vi":
            return f"Chu vi là: {2*(a+b)}"
        elif mess == "Diện tích" or "diện tích":
            return f"Diện tích là: {a*b}"
        else:
            return "Có chút sai sót. Xin hãy nhập lại"

    def H3g(self,mess):
        if mess == "Chu vi" or "chu vi":
            a = float(input("Nhập cạnh thứ nhất: "))
            b = float(input("Nhập cạnh thứ hai: "))
            c = float(input("Nhập cạnh thứ ba: "))
            return "Chu vi là: {a+b+c}"
        elif mess == "Diện tích" or "diện tích":
            print("1: Cạnh\t2: Đáy và cao")
            mess1 = int(input("Chọn:"))
            if mess1 == 1:
                a = float(input("Nhập cạnh thứ nhất: "))
                b = float(input("Nhập cạnh thứ hai: "))
                c = float(input("Nhập cạnh thứ ba: "))
                p = (a+b+c)/2
                return f"Diện tích là: {p*cm.sqrt((p-a)*(p-b)*(p-c))}"
            elif mess1 == 2:
                d = float(input("Nhập đáy: "))
                c = float(input("Nhập chiều cao:"))
                return f"Diện tích là: {d*c/2}"
            else:
                return "Có chút sai sót. Xin hãy nhập lại"
        else:
            return "Có chút sai sót. Xin hãy nhập lại"

    def Htr(self,mess):
        r = float(int("Nhập bán kính: "))
        if mess == "Chu vi" or "chu vi":
            return f"Chu vi là: {2*r*cm.pi}"
        elif mess == "Diện tích" or "diện tích":
            return f"Diện tích là: {cm.pi*r**2}"
        else:
            return "Có chút sai sót. Xin hãy nhập lại"

    def Hcau(self,mess):
        r = float(int("Nhập bán kính: "))
        if mess == "Diện tích xung quanh" or "diện tích xung quanh":
            return f"Diện tích xung quanh: {4*cm.pi*r**2}"
        elif mess == "Thể tích" or "thể tích":
            return f"Thể tích: {4*cm.pi*r**2/3}"
        else:
            return "Có chút sai sót. Xin hãy nhập lại"

    def Htru(self,mess):
        r = float(int("Nhập bán kính: "))
        c = float(input("Nhập chiều cao:"))
        if mess == "Diện tích xung quanh" or "diện tích xung quanh":
            return f"Diện tích xung quanh: {2*cm.pi*r*cm.sqrt(r**2+c**2)}"
        elif mess == "Thể tích" or "thể tích":
            return f"Thể tích: {cm.pi*r*c}"
        else:
            return "Có chút sai sót. Xin hãy nhập lại"

    def Hnon(self,mess):
        r = float(int("Nhập bán kính: "))
        c = float(input("Nhập chiều cao:"))
        if mess == "Diện tích xung quanh" or "diện tích xung quanh":
            return f"Diện tích xung quanh: {cm.pi*r*cm.sqrt(r**2+c**2)}"
        elif mess == "Thể tích" or "thể tích":
            return f"Thể tích: {cm.pi*r*c/3}"
        else:
            return "Có chút sai sót. Xin hãy nhập lại"

    def Hhcn(self,mess):
        a = float(input("Nhập cạnh thứ nhất: "))
        b = float(input("Nhập cạnh thứ hai: "))
        c = float(input("Nhập cạnh thứ ba: "))
        if mess == "Diện tích xung quanh" or "diện tích xung quanh":
            return f"Diện tích xung quanh: {2*(a*b+a*c+b*c)}"
        elif mess == "Thể tích" or "thể tích":
            return f"Thể tích: {a*b*c}"
        else:
            return "Có chút sai sót. Xin hãy nhập lại"

    def Hcho(self):
        s = float(input("Nhập diện tích đáy: "))
        c = float(input("Nhập chiều cao:"))
        return f"Thể tích: {s*c/3}"


class MatrixCalculator():
    def _xu_li(matrix):
        n_matrix = np.zeros(matrix.shape,dtype=float)
        x = matrix.shape[0]
        n_matrix[x-1] = matrix[0]
        n_matrix[:x-1] = matrix[1:]
        return n_matrix

    def rut_gon_ma_tran(self):
        # tạo ma trận
        m = int(input('Enter rows of matrix: '))
        n = int(input('Enter columns of matrix: '))
        matrix = np.zeros((m,n),dtype = float)
        for i in range(m):
            for j in range(n):
                matrix[i,j] = float(input(f"Enter x({i+1},{j+1}): "))
        print('\nYour matrix:\n',matrix,'\n')

        # ktra ma trận đủ điều kiện hay ko
        ktra = False
        while True:
            dem = 0
            for i in range(m):
                if matrix[i,0] == 0: dem += 1               
            if dem == m:
                print("Can't solve the problem")
                break
            elif matrix[0,0] == 0:
                matrix = self._xu_li(matrix)
                ktra = True
                break
            else:
                ktra = True
                break

        # rút gọn ma trận
        if ktra == True:
            if m < n:
                n = m
            for i in range(n):
                if matrix[i,i] != 1:
                    matrix[i] = matrix[i] / matrix[i,i]
                for j in range(m):
                    if j != i:
                        if matrix[j,i] != 0:
                            matrix[j] = matrix[j] + matrix[i]*(-matrix[j,i])
                    print(f'Step {j + i*2 + 1}:\n',matrix)

    def ma_tran_nghich_dao(self):
        m = int(input('Enter tier of square matrix: '))
        matrix = np.zeros((m,m),dtype = float)
        for i in range(m):
            for j in range(m):
                matrix[i,j] = float(input(f"Enter x({i+1},{j+1}): "))
        print('Matrix A:\n',matrix)

        # ghép ma trận và ma trận đơn vị có cùng kích thước 
        n_matrix = np.zeros((m,2*m))
        I_matrix = np.zeros((m,m))
        for i in range(m):
            I_matrix[i,i] = 1
        n_matrix[:,:m] = matrix
        n_matrix[:,m:] = I_matrix

        # ktra ma trận đủ điều kiện hay ko
        ktra = False
        while True:
            dem = 0
            for i in range(m):
                if matrix[i,0] == 0: dem += 1                
            if dem == m:
                print("Can't solve the problem")
                break
            elif n_matrix[0,0] == 0:
                n_matrix = self._xu_li(n_matrix)
                ktra = True
                break
            else:
                ktra = True
                break

        # rút gọn ma trận
        if ktra == True:
            for i in range(m):
                if n_matrix[i,i] != 1:
                    n_matrix[i] = n_matrix[i] / n_matrix[i,i]
                for j in range(m):
                    if j != i:
                        if n_matrix[j,i] != 0:
                            n_matrix[j] = n_matrix[j] + n_matrix[i]*(-n_matrix[j,i])

            print('\nInverse matrix of matrix A:\n',n_matrix[:,m:])

    def dinh_thuc(self):
        # tạo ma trận
        m = int(input('Enter tier of square matrix: '))
        matrix = np.zeros((m,m))
        for i in range(m):
            for j in range(m):
                matrix[i,j] = float(input(f'Enter x({i+1},{j+1}) = '))

        # ktra định dạng ma trận
        ktra = False
        while True:
            dem = 0
            for i in range(m):
                if matrix[i,0] == 0: dem += 1
                
            if dem == m:
                print('Determinant of matrix: det(A) = 0')
                break
            elif matrix[0,0] == 0:
                matrix = self._xu_li(matrix)
                ktra = True
                break
            else:
                ktra = True
                break

        # xử lí, tính toán
        if ktra == True:
            for i in range(m):
                for j in range(i+1,m):
                    matrix[j] = matrix[j] + matrix[i]/matrix[i,i]*(-matrix[j,i])
            det = 1
            for i in range(m):
                det *= matrix[i,i]
            print('Determinant of matrix: det(A) = ',det)

    def giai_he_pt(self):
        # tạo ma trận
        m = int(input('Enter tier of mutilequation: '))
        n = m + 1
        matrix = np.zeros((m,n),dtype = float)
        for i in range(m):
            for j in range(n):
                he_so = ['a','b','c','d']
                matrix[i,j] = float(input(f"Enter {he_so[j]}{i+1}: "))

        # ktra ma trận đủ điều kiện hay ko
        ktra = False
        while True:
            dem = 0
            for i in range(m):
                if matrix[i,0] == 0: dem += 1    
            if dem == m:
                print("Can't solve the problem")
                break
            elif matrix[0,0] == 0:
                matrix = self._xu_li(matrix)
                ktra = True
                break
            else:
                ktra = True
                break

        # rút gọn ma trận
        if ktra == True:
            if m < n:
                n = m
            for i in range(n):
                if matrix[i,i] != 1:
                    matrix[i] = matrix[i] / matrix[i,i]
                for j in range(m):
                    if j != i:
                        if matrix[j,i] != 0:
                            matrix[j] = matrix[j] + matrix[i]*(-matrix[j,i])

            print('Result:\n')
            for i in range(len(matrix[:,-1])):
                print(f'x{i+1} = ',matrix[i,-1])


class Equation():
    def pt1():
        a = float(input("Nhập hệ số a:"))
        b = float(input("Nhập hệ số b:"))
        if a==0 and b == 0:
            return "Phương trình vô số nghiệm"
        elif a == 0:
            return "Phương trình vô nghiệm"
        else:
            return f"Nghiệm của phương trình: {-b/a}"

    def pt2():
        a = float(input("Nhập hệ số a:"))
        b = float(input("Nhập hệ số b:"))
        c = float(input("Nhập hệ số c:"))
        if a != 0:
            delta = b**2 -4*a*c
            n1 = 0
            n2 = 0
            if delta < 0:
                print("Phương trình có hai nghiệm")
                n1 = (-b+cm.sqrt(delta))/(2*a)
                n2 = (-b-cm.sqrt(delta))/(2*a)
                print(f"Nghiệm thứ nhất: {n1}")
                print(f"Nghiệm thứ nhất: {n2}")
            elif delta == 0:
                print(f"Phương trình có nghiệm kép: {-b/(2*a)}")
        else:
            print("Xin hãy xem lại đầu vào")
   
    def pt3():
        a = float(input("Nhập hệ số a:"))
        b = float(input("Nhập hệ số b:"))
        c = float(input("Nhập hệ số c:"))
        d = float(input("Nhập hệ số d:"))

        if a != 0 :
            delta = b**2 - 3*a*c
            k = (9*a*b*c - 2*(b**3) - 27*(a**2)*d)/(2*np.sqrt(abs(delta)**3))

            if delta > 0:
                if abs(k) <= 1:
                    sqrtDelta = np.sqrt(delta)
                    x1 = (2*sqrtDelta*np.cos(np.arccos(k)/3) - b)/(3*a)
                    x2 = (2*sqrtDelta*np.cos(np.arccos(k)/3 - 2*np.pi/3) - b)/(3*a)
                    x3 = (2*sqrtDelta*np.cos(np.arccos(k)/3 + 2*np.pi/3) - b)/(3*a)
                    lst = [x1,x2,x3]
                    print(lst)
                else:
                    x = ((np.sqrt(delta)*abs(k))/(3*a*k))*((abs(k)+np.sqrt(k**2 - 1))**(1/3)+(abs(k) - np.sqrt(k**2 - 1))**(1/3)) - b/(3*a)
                    print(list(x))

            elif delta == 0:
                x = (-b + (b**3 - 27*(a**2)*d)**(1/3))/(3*a)
                print(list(x))

            elif delta < 0:
                x = (np.sqrt(delta)/(3*a))*((abs(k)+np.sqrt(k**2 - 1))**(1/3)+(abs(k) - np.sqrt(k**2 - 1))**(1/3)) - b/(3*a)
                print(list(x))

        else:
            print("Xin hãy xem lại")

    def pt4():
        pass
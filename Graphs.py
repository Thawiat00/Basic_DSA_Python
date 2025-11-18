
# =====================================================
# แบบฝึกหัดที่ 1: Graph
# =====================================================
print("\n📝 แบบฝึกหัดที่ 1: Graph - สร้างกราฟเมืองในจังหวัด")
print("-" * 70)
print("""
โจทย์: สร้างกราฟแสดงระยะทางระหว่างเมือง
- เมือง: อุดร, หนองคาย, สกลนคร, เลย
- ระยะทาง:
  อุดร - หนองคาย: 50 กม.
  อุดร - สกลนคร: 60 กม.
  อุดร - เลย: 150 กม.
  หนองคาย - เลย: 180 กม.
  สกลนคร - เลย: 200 กม.

ให้:
1. สร้างกราฟด้วย Adjacency Matrix
2. แสดงกราฟ
3. หาเมืองที่เชื่อมต่อกับอุดรธานี
""")

# TODO: เขียนโค้ดตรงนี้
print("\n💡 เฉลย:")

class CityGraph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.cities = [''] * size
    
    def add_city(self, index, name):
        self.cities[index] = name
    
    def add_road(self, city1, city2, distance):
        self.adj_matrix[city1][city2] = distance
        self.adj_matrix[city2][city1] = distance
    
    def display(self):
        print("\n  ", end="")
        for city in self.cities:
            print(f"{city:>8}", end="")
        print()
        for i in range(self.size):
            print(f"{self.cities[i]:>5}", end=" ")
            for j in range(self.size):
                print(f"{self.adj_matrix[i][j]:>7}", end="")
            print()
    
    def get_connected_cities(self, city_index):
        connected = []
        for i in range(self.size):
            if self.adj_matrix[city_index][i] != 0:
                connected.append((self.cities[i], self.adj_matrix[city_index][i]))
        return connected

# สร้างกราฟ
g = CityGraph(4)
g.add_city(0, 'อุดร')
g.add_city(1, 'หนองคาย')
g.add_city(2, 'สกลฯ')
g.add_city(3, 'เลย')

g.add_road(0, 1, 50)
g.add_road(0, 2, 60)
g.add_road(0, 3, 150)
g.add_road(1, 3, 180)
g.add_road(2, 3, 200)

g.display()
print(f"\nเมืองที่เชื่อมต่อกับอุดร: {g.get_connected_cities(0)}")
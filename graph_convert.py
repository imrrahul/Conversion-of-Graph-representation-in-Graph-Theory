from collections import defaultdict
import pprint


def adjlist_2_incmat(adjacency_list):
    list_len = len(adjacency_list)
    max_edges = (list_len * (list_len - 1)) / 2
    incident_matrix = [[0] * list_len for _ in xrange(max_edges)]
    current_row = 0
    for parent_vertex, vertices in adjacency_list.iteritems():
        for child_vertex in vertices:
            
            if child_vertex < parent_vertex:
                continue
            incident_matrix[current_row][parent_vertex] = 1
            incident_matrix[current_row][child_vertex] = 1
            current_row += 1
    return incident_matrix


def adjmat_2_adjlist(matrix):
    adjacency_list = defaultdict(list)
    row_len = len(matrix[0])
    nums_cols_to_iter = row_len
    for row_index, row in enumerate(matrix):
        start_from_col = row_len - nums_cols_to_iter
        for col_index, col_val in enumerate(row[start_from_col:],
                                            start_from_col):
            if row_index == col_index:
                continue
            if col_val:
                adjacency_list[row_index].append(col_index)
                adjacency_list[col_index].append(row_index)
        nums_cols_to_iter -= 1
    return dict(adjacency_list)



def adjlist_2_adjmat(aux1):
    matrix=[]
    n=len(aux1)
    l = [x for x in range(0, n)]
    for line in aux1.values():
        

        aux = []
        for key in l:
    
            if key in line:
                aux.append(1)
            else:
                aux.append(0)
        matrix.append(aux)
    return matrix
def adjmat_2_incmat(matrix):
    adjacency_list = adjmat_2_adjlist(matrix)
    Incidence_matrix = adjlist_2_incmat(adjacency_list)
    return Incidence_matrix


print("1. Convert Adj mat to Adj list\n 2. Convert Adj list to Adj matrix.\n 3. Convert Incd. matrix to Adj list\n 4. Convert Adj list to Adj matrix\n 5. Convert Adj matrix to Incd. matrix\n 6. Convert Incd. matrix to Adj matrix");
choice = input("Enter what you want to convert:\n")
if(choice=="1"):
  print("Adj mat to Adj list")

  matrix=[]
  matrix.append([0, 0, 0, 1, 1, 0])
  matrix.append([1, 1, 1, 0, 0, 1])
  matrix.append([0, 0, 0, 0, 0, 1])
  matrix.append([1, 1, 1, 1, 1, 0])
  matrix.append([1, 0, 0, 1, 1, 1])
  matrix.append([1, 1, 1, 1, 1, 1])
  print("Input Adj matrix")
  pprint.pprint(matrix)
  print("Output Adj List")
  
  pprint.pprint(adjmat_2_adjlist(matrix))
def incdmat_2_Adjlist(matrix):
    adjacency_list = defaultdict(list)
    def add_edge(x, y):
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    for vertices in matrix:
        pairs = []
        for index, v in enumerate(vertices):
            if v:
                pairs.append(index)
        add_edge(*pairs)
    return dict(adjacency_list)
if(choice=="2"):
  print("Adj list to Adj mat") 
  adj_list = {0: [1, 2, 4, 5],
                     1: [0, 2, 3, 5],
                     2: [0, 1, 3,],
                     3: [2, 4, 5],
                     4: [0, 1, 2, 3, 5],
                     5: [0, 4]}
  print("Adj list as input ")
  pprint.pprint(adj_list)
  print("Output Adj matrix")
  
  pprint.pprint(adjlist_2_adjmat(adj_list)) 
def incmat_2_adjmat(matrix):
    adjacency_list = incdmat_2_Adjlist(matrix)
    adjacency_matrix = adjlist_2_incmat((adjacency_list))
    return adjacency_matrix

if(choice=="3"):
  print("Incidence mat to Adj list")
  incident_matrix = [[1, 0, 0, 1, 1, 0],
                          [1, 0, 0, 0, 1, 0],
                          [0, 0, 0, 1, 0, 0],
                          [1, 1, 0, 0, 1, 1],
                          [0, 0, 0, 0, 0, 1],
                          [0, 1, 1, 0, 1, 0],
                          [1, 1, 0, 1, 0, 1],
                          [1, 1, 1, 0, 1, 1]]
  print("Input incidence matrix")
  pprint.pprint(incident_matrix)
  print("Output Adj list")
  
  pprint.pprint(incdmat_2_Adjlist(incident_matrix))
if(choice=="4"):
  print("Adj list to Adj mat")
  adj_list = {0: [1, 3, 4, 5],
                     1: [1, 2, 4, 5],
                     2: [0, 1, 5],
                     3: [0, 1, 2],
                     4: [0, 1, 3, 5],
                     5: [0, 1, 2, 3, 4]}
  print("Input Adj list")
  pprint.pprint(adj_list)
  print("Output Adj matrix")
  
  pprint.pprint(adjlist_2_adjmat(adj_list))
if(choice=="5"):
  print("Adj mat to Incidence mat")
  matrix = []
  matrix.append([0, 0, 0, 1, 1, 0])
  matrix.append([1, 1, 1, 0, 0, 1])
  matrix.append([0, 0, 0, 0, 0, 1])
  matrix.append([1, 1, 1, 1, 1, 0])
  matrix.append([1, 0, 0, 1, 1, 1])
  matrix.append([1, 1, 1, 1, 1, 1])
  print("Input adjacent matrix")
  pprint.pprint(matrix)
  print("Output Incident matrix")
  
  pprint.pprint(adjmat_2_incmat(matrix))
if(choice=="6"):
  print("Incident matrix to Adj matrix")
  incident_matrix = [[1, 0, 0, 1, 1, 0],
                          [1, 0, 0, 0, 1, 0],
                          [0, 0, 0, 1, 0, 0],
                          [1, 1, 0, 0, 1, 1],
                          [0, 0, 0, 0, 0, 1],
                          [0, 1, 1, 0, 1, 0],
                          [1, 1, 0, 1, 0, 1],
                          [1, 1, 1, 0, 1, 1]]
  print("Input Incident Matrix")
  pprint.pprint(incident_matrix)
  print("Output Adj matrix")
  pprint.pprint(incmat_2_adjmat(incident_matrix))
  

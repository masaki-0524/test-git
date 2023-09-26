M = int(input().rstrip())
R_p = []
D_p = []
pre_point = [0 for i in range(M)]
point = [0 for i in range(M)]
for i in range(M):
  data = input().rstrip()
  if data == "Republican":
    R_p.append(i)
  elif data == "Democratic":
    D_p.append(i)
N = int(input().rstrip())
v = [[-1 for i in range(M)] for k in range(N)]
for i in range(N):
  v[i] = [int(a)-1 for a in input().rstrip().split(' ')]

for i in range(N):
  R_p_data = 0
  D_p_data = 0
  for k in range(M):
    if v[i][k] in R_p:
      R_p_data += 1
      if R_p_data < 2:
        pre_point[v[i][k]] += 1

    elif v[i][k] in D_p:
      D_p_data += 1
      if D_p_data < 2:
        pre_point[v[i][k]] += 1
    
    if R_p_data == 1 and D_p_data == 1:
      break



pre_point_index = [i[0] for i in sorted(enumerate(pre_point), key=lambda x:x[1])]

pre_point_index.reverse()
final_list = []
not_final_list = []
R_p_data_index = 0
D_p_data_index = 0
for a in pre_point_index:
  if a in R_p:
    R_p_data_index += 1
    if R_p_data_index <2:
      final_list.append(a)
    else:
      not_final_list.append(a)
  else:
    D_p_data_index += 1
    if D_p_data_index <2:
      final_list.append(a)
    else:
      not_final_list.append(a)

for i in range(N):
  for k in range(M):
    if v[i][k] == final_list[0]:
      point[final_list[0]] += 1
      break
    if v[i][k] == final_list[1]:
      point[final_list[1]] += 1
      break
max_data = max(point)
max_index = point.index(max_data)


print(max_index+1)
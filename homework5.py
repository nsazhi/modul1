str_ = 'string'
int_ = 25
bool_ = True
mutable_list_ = [1, 2, 3]
immutable_var = (str_,int_,bool_,mutable_list_)
print(immutable_var)
str_ = 'new_string'
int_ = 35
bool_ = False
mutable_list_ = [4, 5, 6]
print(immutable_var) # элементы внутри кортежа отсались неизменными, т.к. это неизменяемая коллекция
immutable_var[3][0] = 4
immutable_var[3][1] = 5
immutable_var[3][2] = 6
print(immutable_var)
class utils:



    def forma(self, dict1):
        list1 = []
        dict2 = {}
        for key in dict1.keys():
           if '{' in dict1.get(key):
               dict2 = dict1.get(key)
           else:
               list1.append({key, dict1.get(key)})

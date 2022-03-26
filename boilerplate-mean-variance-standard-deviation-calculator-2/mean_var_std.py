import numpy as np

def calculate(list):
  #Raise error:
  if len(list) > 9 or len(list) < 9:
    raise ValueError ('"List must contain nine numbers."')
  #create numpy array from a list:
  new_array = np.array(list).reshape((3,3))

  task_list = ['mean','variance','standard deviation','max','min','sum']
  dispatcher = ['mean', 'var', 'std', 'max', 'min', 'sum']

  calculations = {task_list[task]: [np.array(getattr(np,dispatcher[task])(new_array,axis=0)).tolist(),
                                    np.array(getattr(np,dispatcher[task])(new_array,axis=1)).tolist(),
                                    np.array(getattr(np,dispatcher[task])(new_array)).tolist()] for task in range(0,len(task_list))}
  return calculations
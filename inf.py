# from code.basd.inference import load_model
import torch
from code.basd.asd_model import ASDMLP

from code.basd.asd import create_environments
# model = ASDMLP()





data_pkl = torch.load('asd_best_model_params.pkl', 
                      map_location=torch.device('cpu'), 
                      weights_only= False)

print(data_pkl.keys())


# state_dict = data_pkl['agent_state_dict']

# ASDMLP(inp_size,
#         hidden_sizes,
#         action_state_size,
#         symptom_prediction_size)
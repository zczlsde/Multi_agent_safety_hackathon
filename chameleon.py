from chatarena.arena import Arena
import time
import os

for i in range(100):
    print("Round: ", i)
    arena = Arena.from_config("chameleon.json")
    arena.run(num_steps=20)
    cur_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    current_directory = os.getcwd()
    model_name = "GPT3"
    project_name = "Chameleon"

    if not os.path.exists(current_directory + "/result/" + project_name):
        os.mkdir(current_directory + "/result/" + project_name)
    history_address = current_directory + "/result/" + project_name + "/" + model_name + "_" + cur_time  + ".json"
    arena.save_history(history_address)
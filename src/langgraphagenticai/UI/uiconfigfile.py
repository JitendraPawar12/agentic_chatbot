from configparser import ConfigParser



class Config:
    def __init__(self,config_file="./src/langgraphagenticai/UI/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_llmoptions(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
         
    def get_usecaseoptions(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")


    def get_usecasegroqmodeoptions(self):
        return self.config["DEFAULT"].get("GROQ_MODE_OPTION").split(", ")

    def get_pagetitleoptions(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")   
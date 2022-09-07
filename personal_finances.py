import json

class Register:
    # this class can be either an increase\decrease value instance
    def __init__(self, name: str, value: float) -> None:
        self.__name = name
        self.__value = value

    @property
    def name(self): return self.__name

    @property
    def value(self): return self.__value

class Month:
    # storing entries for later .json and\or Pandas.DataFrame
    def __init__(self, name) -> None:
        self.__inputs = []
        self.__outputs = []
        self.__log = {}

        self.__name = name

    @property
    def log(self) -> dict: return self.__log

    def add_input (self, name: str, value: float):
        self.__inputs.append(Register(name, value))

    def add_output (self, name:str, value: float):
        self.__outputs.append(Register(name, value))

    def add_output_perc(self, name: str, perc: float):
        value = self.balance * (perc / 100)
        self.__outputs.append(Register(name, value))
    
    @property
    def total_input(self) -> float:
        total_input = 0
        for input in self.__inputs:
            total_input += input.value
        return total_input

    @property
    def balance(self) -> float:
        total_output = 0
        for output in self.__outputs:
            total_output += output.value
        return self.total_input - total_output

    def create_log(self) -> list:
        all_values = []
        all_ops = []
        all_names = []
        for input in self.__inputs:
            all_values.append(input.value)
            all_ops.append("input")
            all_names.append(input.name)
        for output in self.__outputs:
            all_values.append(output.value)
            all_ops.append("output")
            all_names.append(output.name)
        
        all_names.append("Balance")
        all_ops.append("---")
        all_values.append(self.balance)

        self.__log["Name"] = all_names
        self.__log["Op"] = all_ops
        self.__log["Value"] = all_values

        return self.log

    def log_file (self) -> None:
        outfile = open(f"{self.__name}.json", "w")
        outfile.write(json.dumps(self.log, indent=4))
        outfile.close()
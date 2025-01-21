class ConfigTypeError(Exception):
    def __init__(self, err_type, widget, err_part):
        super().__init__(f"{err_type} in \"addons\\{widget}\\parameterConfig.json\"\n"
                         f"{err_part}\n"
                         f"{' ' * err_part.find(err_type) + '^' * len(err_type)}")

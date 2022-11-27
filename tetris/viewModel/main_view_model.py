from ..model.reactive_model import ReactiveModel


class MainViewModel(ReactiveModel):
    state: str
    complexity: int


app_model = MainViewModel()
# app_model.expression = ""
# app_model.deg = True
app_model.state = "menu"


# # спустя время
# app_model.complexity = 3
# app_model.state = "menu"

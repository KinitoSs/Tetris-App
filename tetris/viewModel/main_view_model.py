from ..model.reactive_model import ReactiveModel


class MainViewModel(ReactiveModel):
    state: str
    complexity: int


app_model = MainViewModel()
app_model.state = "menu"

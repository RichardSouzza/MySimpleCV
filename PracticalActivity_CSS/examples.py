class Example:
    def __init__(self, number, title, type="topic"):
        self.number = number
        self.title = title
        self.route = f"/PracticalActivity-CSS/example-{number.replace('.', '-')}"
        self.type = type


examples = [
    Example("1", "Primeiro Exemplo"),
    Example("2", "Seletor ID"),
    Example("3", "Seletor de Classe"),
    Example("4", "Seletor de Classe Específica"),
    Example("5", "Seletor de Múltiplas Classes"),
    Example("6", "Agrupamento de Seletores"),
    Example("7", "Comentários"),
    Example("8", "Cores"),
    Example("9", "Cor de Fundo"),
    Example("10", "Cor de Texto"),
    Example("11", "Cor das Bordas"),
    Example("12", "Valores das Cores"),
    Example("13", "Valores RGB"),
    Example("14", "Valores HEX"),
    Example("15", "Tons de Cinza"),
    Example("16", "Fundo (Backgrounds)"),
    Example("16.1", "Cor de Fundo", "subtopic"),
    Example("16.2", "Cor de Fundo 2", "subtopic"),
    Example("16.3", "Imagem de Fundo", "subtopic"),
    Example("17", "Borda (Border)"),
    Example("17.1", "Estilos de Bordas (border-style)", "subtopic"),
    Example("17.2", "Largura da Borda (border-width)", "subtopic"),
    Example("17.3", "Cor da Borda (border-color)", "subtopic"),
    Example("18", "Margem (Margin)"),
    Example("18.1", "Margem - Propriedade Abreviada", "subtopic"),
    Example("18.2", "Margem - Valor auto", "subtopic"),
    Example("19", "Preenchimento (Padding)"),
    Example("19.1", "Padding e Width (sem box-sizing)", "subtopic"),
    Example("19.2", "Padding e Width (com box-sizing)", "subtopic"),
    Example("20", "Altura e Largura (Height e Width)"),
    Example("20.1", "Largura Máxima (max-width)", "subtopic"),
    Example("21", "Formatação de Texto"),
]


from google.adk.agents.llm_agent import Agent


def explicar_concepto(concepto: str) -> dict:
    """Explica conceptos relacionados con informática."""

    conceptos = {
        "api": "Una API permite comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "python": "Python es un lenguaje de programación.",
        "inteligencia artificial": "La IA permite realizar tareas inteligentes.",
        "servidor": "Un servidor proporciona servicios a otros equipos.",
        "variable": "Una variable almacena un valor.",
        "software": "El software es el conjunto de programas de un sistema."
    }

    if not isinstance(concepto, str) or not concepto.strip():
        return {
            "status": "error",
            "explicacion": "Debes ingresar un concepto válido."
        }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado."
    }


def calcular_promedio(notas: list[float]) -> dict:
    """Calcula el promedio de notas entre 0 y 20."""

    if not notas or any(
        isinstance(n, bool)
        or not isinstance(n, (int, float))
        or not 0 <= n <= 20
        for n in notas
    ):
        return {
            "status": "error",
            "mensaje": "Ingresa notas válidas entre 0 y 20."
        }

    promedio = round(sum(notas) / len(notas), 2)

    return {
        "status": "success",
        "promedio": promedio
    }


root_agent = Agent(
    model="gemini-3.6-flash",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico de Ingeniería de Sistemas.
    Responde siempre en español.
    Utiliza un lenguaje sencillo.
    Explica conceptos informáticos.
    Calcula promedios cuando el usuario lo solicite.
    Usa las herramientas disponibles cuando corresponda.
    """,
    tools=[explicar_concepto, calcular_promedio],
)

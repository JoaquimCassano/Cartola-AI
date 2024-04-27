import cartolafc, sys
sys.path.append(r"C:\Users\joaqu\Downloads\Cartola-AI\src")
import players
api = cartolafc.Api()
print(api.mercado_atletas()[0].clube)

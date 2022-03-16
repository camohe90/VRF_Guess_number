# Adivina el número

En este repositorio vamos mejorar el contrato básico de [Guess number](https://github.com/camohe90/guess_number)para agregarle la funcionaldiad de [números aleatorios](https://www.youtube.com/watch?v=eRzLNfn4LGc&feature=emb_imp_woyt) que nos provee chainlink.

Tomando como base el uso de VRF2 y la explicación para la implementación del canal de youtube de Chainlink -> https://youtu.be/yJQJ7pw_9C0

## Prerequisitos

Por favor instale o tenga instalado lo siguiente:

- [nodejs y npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)

## Instalación

1. [Instalar brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), sino lo haz hecho, esta es una forma sencilla de hacerlo.


```bash
pip install eth-brownie
```
Sino funciona podrias hacerlo via pipx
```bash
pip install --user pipx
pipx ensurepath
# restart your terminal
pipx install eth-brownie
```

2. Configura las variables de entorno

Configura tus [variables de entorno](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) `WEB3_INFURA_PROJECT_ID`, y `PRIVATE_KEY` . 

Puedes obtener un `WEB3_INFURA_PROJECT_ID` creando una cuenta en [Infura](https://infura.io/). Creas un nuevo proyecto y seleccionas la red de pruebas rinkeby. 

En cuanto a tu `PRIVATE_KEY` las puedes obtener de una wallet como [metamask](https://metamask.io/). 

Tambien vas a necesitar ETH rinkeby de prueba. Puedes obtener ETH usando el siguiente [faucet de rinkeby en el siguiente enlace](https://faucets.chain.link/rinkeby). 
Si eres nuevo por favor, [mira este video.](https://www.youtube.com/watch?v=P7FX_1PePX0)

Puedes agregar tus variables de entorno en el archivo `.env`:

```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

Luego, debes estar seguro que tu archivo `brownie-config.yaml` tenga:

```
dotenv: .env
```

## ¿Qué necesitamos?

- Comprueba en MetaMask que tienes testnet ETH y LINK en Rinkeby. Si necesitas fondos de testnet, puedes conseguirlos en [faucer](faucets.chain.link)
- Ingresar al [Chainlink Verificable Randomness Function](https://vrf.chain.link/) y crear una subscripción, para ello debes ingresar la billetera desde la cual vas a enviar los links para ejecutar este servicio. 
- Una vez creada la subscripción se te asignara un ID, que será el que usemos en el arhcivo brownieconfig.yaml en la linea 59.

O tambien puedes ejecutar el siguiente comando para que se crea la subscripción al servicio de VRF de chainlink

```
brownie run scripts/vrf_scripts/create_subscription.py --network rinkeby
```

## Iniciando con el VRF de chainlink

Para cada solicitud, Chainlink VRF genera uno o más valores aleatorios y una prueba criptográfica de cómo se determinaron esos valores. La prueba se publica y se verifica en la cadena antes de que cualquier aplicación consumidora pueda utilizarla. Este proceso garantiza que los resultados no puedan ser manipulados por ninguna entidad, incluyendo operadores de oráculo, mineros, usuarios o desarrolladores de contratos inteligentes.


## Ahora si estamos listos 

Ahora debemos ejecutar el script deploy_vrf_consumer con el cual vamos a desplegar el contrato inteligente para consumir el servicio de VRF para ello debemos ejecutar el siguiente comando

```bash
brownie run scripts/vrf_scripts/01_deploy_vrf_consumer.py --network rinkeby 
```

Si al ejecutar este comando se despliega el contrato correctamente deberian recibir un mensaje como el siguiente

Ahora debemos hacer la solicitud del número aleaotorio qué es aquel el cual los jugadores intentaran adivinar, para ello usaremos el siguiente comando.

```bash
brownie run scripts/vrf_scripts/02_request_randomness.py --network rinkeby
```

Debemos esperar aproximadamente 1 minuto mientras se consume el servicio y se obtiene el número aleatorio, ahora podemos jugar apostando minimo 0.1 ethers para adivinar el número, podriamos ver el saldo que tiene el contrato inteligente o si somos la cuenta que desplego el contrato (Owner) podriamos consultar el número que nos genero el VRF


## Recursos

Para empezar con brownie:

* [Documentación chainlink](https://docs.chain.link/docs)
* Revisa la [Documentación chainlink](https://docs.chain.link/docs) para dar esos primeros pasos en el desarrollo de contratos ingeligentes
* Puedes revisar los otros [Brownie mixes](https://github.com/brownie-mix/) que pueden ser usado como punto de partida para tus propios contratos. Allí encontraras ejemplos para emepzar como.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) es un buen tutorial para que te familiarices con Brownie.
* Para más información especifica, puedes revisar la [documentación Brownie](https://eth-brownie.readthedocs.io/en/stable/).

## Licencia

This project is licensed under the [MIT license](LICENSE).
Basado en el repositorio [chainlink mix](https://github.com/smartcontractkit/chainlink-mix)


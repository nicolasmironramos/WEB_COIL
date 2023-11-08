<link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
<script defer src="https://pyscript.net/latest/pyscript.js"></script>

<py-config>
    packages = [
        "matplotlib"
    ]
    plugins = [
        "https://pyscript.net/latest/plugins/python/py_tutor.py"
    ]
</py-config>
<script type="py">
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt 
    from google.colab import drive

    drive.mount("/content/drive")
    df_accidentes = pd.read_excel("/content/drive/MyDrive/AccidentesBicicletas_2023.xlsx")
    df_accidentes

    df_accidentes.isna().sum()

    df_accidentes["estado_meteorológico"]=df_accidentes["estado_meteorológico"].fillna(value="Se desconoce")
    conteo_edomet = df_accidentes["estado_meteorológico"].value_counts()
    print(conteo_edomet)

    conteo_edomet.plot(kind="bar")
    plt.xlabel("Estado Meteorologico")
    plt.ylabel("Frecuencia")
    plt.title("Estado metereologico cuando ocurre accidente")

    conteo_edomet.plot(kind="bar")
    plt.xlabel("Estado Meteorologico")
    plt.ylabel("Frecuencia")
    plt.title("Estado metereologico cuando ocurre accidente")

    df_accidentes["tipo_accidente"]=df_accidentes["tipo_accidente"].fillna(value="NULL")
    conteo_edomet2 = df_accidentes["tipo_accidente"].value_counts()
    print(conteo_edomet2)

    conteo_edomet2.plot(kind="bar")
    plt.xlabel("Accidente")
    plt.ylabel("Frecuencia")
    plt.title("Tipo de accidente")

    df_accidentes["tipo_vehiculo"]=df_accidentes["tipo_vehiculo"].fillna(value="NULL")
    conteo_edomet3 = df_accidentes["tipo_vehiculo"].value_counts()
    print(conteo_edomet3)

    conteo_edomet3.plot(kind="bar")
    plt.xlabel("Vehiculo")
    plt.ylabel("Frecuencia")
    plt.title("Tipo de Vehiculo")

    df_accidentes["tipo_persona"]=df_accidentes["tipo_persona"].fillna(value="NULL")
    conteo_edomet4 = df_accidentes["tipo_persona"].value_counts()
    print(conteo_edomet4)

    conteo_edomet4.plot(kind="bar")
    plt.xlabel("Persona")
    plt.ylabel("Frecuencia")
    plt.title("Tipo de persona")

    df_accidentes["sexo"]=df_accidentes["sexo"].fillna(value="NULL")
    conteo_edomet5 = df_accidentes["sexo"].value_counts()
    print(conteo_edomet5)

    conteo_edomet5.plot(kind="bar")
    plt.xlabel("Sexo")
    plt.ylabel("Frecuencia")
    plt.title("Sexo de accidentado")

    df_accidentes["lesividad"]=df_accidentes["lesividad"].fillna(value="NULL")
    conteo_edomet6 = df_accidentes["lesividad"].value_counts()
    print(conteo_edomet6)

    conteo_edomet6.plot(kind="bar")
    plt.xlabel("Lesion")
    plt.ylabel("Frecuencia")
    plt.title("Lesividad de accidente") 

    df_accidentes["distrito"]=df_accidentes["distrito"].fillna(value="NULL")
    conteo_edomet7 = df_accidentes["distrito"].value_counts()
    print(conteo_edomet7)

    conteo_edomet7.plot(kind="bar")
    plt.xlabel("Distrito")
    plt.ylabel("Frecuencia")
    plt.title("Distrito donde ocurrio el accidente")

    print("El promedio del codigo de distrito")
    print(df_accidentes["cod_distrito"].mean())
</script>

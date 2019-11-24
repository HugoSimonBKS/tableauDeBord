import json

# TODO: opti le code

urlFichier = "settings.txt"
urlJson = "defaultSettings.json"

# class to create an exception
class InvalidParamError(Exception):
    pass

# reset to default settings in case of error
def resetDefault():
    with open(urlJson) as f:
        d = json.load(f)
        setParams(d)
    f.close()

# read the params in settings.txt
def getParams(lignes):
    tab_asso = dict()
    # read the params line by line while skipping comments
    for ligne in lignes:
        if "#" in ligne:
            pass
        else:
            lig = ligne.split('=')
            tab_asso[lig[0]] = lig[1].replace("\n", "")
    return tab_asso

# get the length of the actual params without comments
def settingsLength():
    f = open(urlFichier)
    count = 0
    lignes = f.readlines()
    f.close()
# skip the comments
    for ligne in lignes:
        if "#" not in ligne:
            count += 1
    return count

# Change the parameters  in settings.txt, if there is an error, ask to reset
def setParams(params):
    f = open(urlFichier)
    lignes = f.readlines()
    f.close()
    i = 0
    # the number of parameters to set must be the same as the number of params already set
    if(not params or len(params) != settingsLength()):
        raise InvalidParamError("Error number of parameters expected invalid", "length expected : ", str(settingsLength()), "length of the parameters recieved : ", str(len(params)))

        #re-write the params with new values
    for param in params:
        # skip comments
        while "#" in lignes[i]:
            i+= 1
        # replace lines
        if(lignes[i] != (param+"="+str(params[param])+"\n")):
            lignes[i] = lignes[i].replace(lignes[i], (param+"="+str(params[param])+"\n"))
        if(i < len(lignes)):
            i += 1

    f = open(urlFichier,'w')
    for j in range(len(lignes)):
        f.write(lignes[j])
    f.close()

# code a foutre dans une fonction
f = open(urlFichier)
lignes  = f.readlines()
f.close()

print(getParams(lignes))
# params = getParams(lignes)
# params["size"] = 30
# setParams(params)
f = open(urlFichier)
newParams = f.readlines()
f.close()


# try:
#     setParams(params)
# except InvalidParamError as err:
#     askReset(err);


print(newParams)

class Thing:
    def __init__(self, name, value1, value2, value3, value4):
        self.name = name
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4

    def toggleCurrent(self):
        pass

    def canSee(self, value):
        pass

    def addFeeling(self, feeling):
        pass

    def requestExecution(self, world):
        pass

    def getDimensions(self):
        pass
        
    def resetDimensions(self):
        pass

    def getCircumference(self):
        pass

    def resetCircumference(self):
        pass

    def getTangent(self, x):
        pass

    def setLimit(self, value):
        pass

    def getNumSimulationsAvailable(self):
        pass

    def toSatisfaction(self):
        pass

    def getFeelingIndex(self, feeling):
        pass

    def getNutrients(self):
        pass

    def resetNutrients(self):
        pass

    def getAntioxidants(self):
        pass

    def resetAntioxidants(self):
        pass

    def purr(self):
        pass

    def toggleGender(self):
        pass

    def toggleRoleBDSM(self):
        pass

    def lookFor(self, thing, world):
        pass

    def setProof(self, value):
        pass

    def getSenseIndex(self, sense):
        pass

    def removeFeeling(self, feeling):
        pass

    def setOpinion(self, index, value):
        pass

    def getOpinionIndex(self, opinion):
        pass

    def escape(self, world):
        pass

    def learnTopic(self, topic):
        pass

    def takeExamTopic(self, topic):
        pass

    def getAlgebraicExpression(self, topic):
        pass

    def escape(self, topic):
        pass
        
class Lovable(Thing):
    def __init__(self, name, value1, value2, value3, value4):
        super().__init__(name, value1, value2, value3, value4)


class Circle(Thing):
    def __init__(self, name, value1, value2, value3, value4):
        super().__init__(name, value1, value2, value3, value4)


class SineWave(Thing):
    def __init__(self, name, value1, value2, value3, value4):
        super().__init__(name, value1, value2, value3, value4)


class Sequence(Thing):
    def __init__(self, name, value1, value2, value3, value4):
        super().__init__(name, value1, value2, value3, value4)


class Eggplant(Thing):
    def __init__(self, name, value1, value2, value3, value4):
        super().__init__(name, value1, value2, value3, value4)


class Tomato(Thing):
    def __init__(self, name, value1, value2, value3, value4):
        super().__init__(name, value1, value2, value3, value4)


class TabbyCat(Thing):
    def __init__(self, name, value1, value2, value3, value4):
        super().__init__(name, value1, value2, value3, value4)

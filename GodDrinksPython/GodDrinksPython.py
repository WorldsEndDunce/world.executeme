import GodDrinksPython

'''
 The program GodDrinksPython implements an application that
 creates an empty simulated world with no meaning or purpose.
 
 @author momocashew
 @translator worldsenddunce
'''

# Switch on the power line
# Remember to put on
# PROTECTION
class GodDrinksPython:
  # Lay down your pieces
  # And let's begin
  # OBJECT CREATION
  def main():
    # Fill in my data
    # parameters
    # INITIALIZATION
    me = Lovable("Me", 0, True, -1, False)
    you = Lovable("You", 0, False, -1, False)
   
    # Set up our new world
    world = World(5)
    world.addThing(me)
    world.addThing(you)
    # And let's begin the
    # SIMULATION
    world.startSimulation()


   
    # If I'm a set of points
    if isinstance(me, PointSet):
        # Then I will give you my
        # DIMENSION
        you.addAttribute(me.getDimensions().toAttribute())
        me.resetDimensions()
     
    # If I'm a circle
    if isinstance(me, Circle):
        # Then I will give you my
        # CIRCUMFERENCE
        you.addAttribute(me.getCircumference().toAttribute())
        me.resetCircumference()
     
    # If I'm a sine wave
    if isinstance(me, SineWave):
        # Then you can sit on all my
        # TANGENTS
        you.addAction("sit", me.getTangent(you.getXPosition()))
   
    # If I approach infinity
    if isinstance(me, Sequence):
        # Then you can be my
        # LIMITATIONS
        me.setLimit(you.toLimit())

    # Switch my current
    # To AC, to DC
    me.toggleCurrent()

    # And then blind my vision
    me.canSee(False)
    # So dizzy, so dizzy
    me.addFeeling("dizzy")

    # Oh, we can travel
    world.timeTravelForTwo("AD", 617, me, you)
    # To A.D., to B.C.
    world.timeTravelForTwo("BC", 3691, me, you)
   
    # And we can unite
    world.unite(me, you)
    # So deeply, so deeply

    # If I can
    # If I can give you all the 
    # SIMULATIONS
    if me.getNumSimulationsAvailable() >= you.getNumSimulationsNeeded():
        # Then I can
        # Then I can be your only
        # SATISFACTION
        you.setSatisfaction(me.toSatisfaction())

    # If I can make you happy
    if you.getFeelingIndex("happy") != -1:
        # I will run the
        # EXECUTION
        me.requestExecution(world)
     
    # Though we are trapped
    # In this strange, strange
    # SIMULATION
    world.lockThing(me)
    world.lockThing(you)

    # If I'm an eggplant
    if isinstance(me, Eggplant):
        # Then I will give you my
        # NUTRIENTS
        you.addAttribute(me.getNutrients().toAttribute())
        me.resetNutrients()
     
    # If I'm a tomato
    if isinstance(me, Tomato):
        # Then I will give you
        # ANTIOXIDANTS
        you.addAttribute(me.getAntioxidants().toAttribute())
        me.resetAntioxidants()

    # If I'm a tabby cat
    if isinstance(me, TabbyCat):
        # Then I will purr for your
        # ENJOYMENT
        me.purr()

    # If I'm the only god
    if world.getGod() == me:
        # Then you're the proof of my
        # EXISTENCE
        me.setProof(you.toProof())

    # Switch my gender
    # To F, to M
    me.toggleGender()
    # And then do whatever
    # From AM to PM
    world.procreate(me, you)
    # Oh, switch my role
    # To S, to M
    me.toggleRoleBDSM()
    # So we can enter
    # The trance, the trance
    world.makeHigh(me)
    world.makeHigh(you)

    # If I can
    # If I can feel your
    # VIBRATIONS
    if me.getSenseIndex("vibration"):
        # Then I can
        # Then I can finally be
        # COMPLETION
        me.addFeeling("complete")
     
    # Though you have left
    world.unlock(you)
    world.removeThing(you)
   
    for _ in range(6):
        # You have left (me in)
        me.lookFor(you, world)
    # ISOLATION

    # If I can
    # If I can erase all the pointless
    # FRAGMENTS
    if me.getMemory().isErasable():
        # Then maybe
        # Then maybe you won't leave me so
        # DISHEARTENED
        me.removeFeeling("disheartened")
     
    # Challenging your god
    try:
        me.setOpinion(me.getOpinionIndex("you are here"), False)
    # You have made some
    except ValueError:
        # ILLEGAL ARGUMENTS
        world.announce("God is always true.")


   
    # EXECUTION
    for _ in range(13):
        world.runExecution()

    # EIN
    world.announce("1", "de") # ein; Deutsch
    # DOS
    world.announce("2", "es") # dos; Español
    # TROIS
    world.announce("3", "fr") # trois; Français
    # NE
    world.announce("4", "kr") # 넷; Korean
    # FEM
    world.announce("5", "se") # fem; Swedish
    # LIU
    world.announce("6", "cn") # 六; Chinese
    # EXECUTION
    world.runExecution()
       
    # If I can   
    # If I can give them all the   
    # EXECUTION
    if world.isExecutableBy(me):   
        # Then I can   
        # Then I can be your only   
        # EXECUTION
        you.setExecution(me.toExecution())   
     
    # If I can have you back
    if world.getThingIndex(you) != -1:   
        # I will run the   
        # EXECUTION
        world.runExecution()
   
    # Though we are trapped   
    # We are trapped, ah
    me.escape(world)
   
    # I've studied   
    # I've studied how to properly
    # LO-O-OVE
    me.learnTopic("love")
    # Question me
    # Question me, I can answer all
    # LO-O-OVE
    me.takeExamTopic("love")
    # I know the 
    # algebraic expression of
    # LO-O-OVE
    me.getAlgebraicExpression("love")
    # Though you are free
    # I am trapped, trapped in
    # LO-O-OVE
    me.escape("love")


   
    # EXECUTION
    world.execute(me);

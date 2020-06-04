from textattack.search_methods import GreedyWordSwapWIR
from textattack.shared.attack import Attack
from textattack.constraints.grammaticality import PartOfSpeech
from textattack.constraints.pre_transformation import RepeatModification, StopwordModification
from textattack.constraints.semantics.sentence_encoders import UniversalSentenceEncoder
from textattack.transformations import CompositeTransformation, WordDeletion
from textattack.goal_functions import UntargetedClassification

def InputReductionFeng2018(model):
    """
    Feng, Wallace, Grissom, Iyyer, Rodriguez, Boyd-Graber. (2018).
    
    Pathologies of Neural Models Make Interpretations Difficult.
 
    ArXiv, abs/1804.07781.
    """
    # At each step, we remove the word with the lowest importance value until 
    # the model changes its prediction.
    transformation = WordDeletion()
    
    constraints = [
        RepeatModification(),
        StopwordModification()
    ]
    #
    # "During the iterative reduction process, we ensure that the prediction 
    # does not change (exact same span for SQUAD); consequently, the model 
    # accuracy on the reduced examples is identical to the original."
    goal_function = UntargetedClassification(model)
    #
    # "For each word in an input sentence, we measure its importance by the 
    # change in the confidence of the original prediction when we remove
    # that word from the sentence."
    #
    # "Instead of looking at the words with high importance values—what 
    # interpretation methods commonly do—we take a complementary approach
    # and study how the model behaves when the supposedly unimportant words are 
    # removed."
    #
    search_method = GreedyWordSwapWIR(wir_method='delete', ascending=True)
        
    return Attack(goal_function, constraints, transformation, search_method)

# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello! This Tarot. What's your first card?"
        reprompt_text = "What's the name of your card? One is The Fool"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CaptureTarotIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureCardIntent")(handler_input)
   
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        card = slots["card"].value
        cardDic = {"the fool":"I sense inexperience.  Perhaps the subject represents a dreamer, someone who may be impulsive and careless.",
            "the magician":"There is harmonious interaction between idea and feeling, desire and emotion.  The subject has organizational skills and creative talents, and the potential to create.",
            "the high priestess":"Here we have spiritual enlightenment and inner illumination.  There may be hidden influences at work.",
            "the empress":"I see material wealth, marriage, and fertility.  There is a nurturing component.",
            "the emperor":"There is stability, law and order.  There is an active force representing authority, leadership, drive and determination.",
            "the hierophant":"I see ritual and ceremony, and an interest in learning.  The subject values social approval and conforms to society's expectations.",
            "the lovers":"I sense that there are difficult decisions, choice, and temptation related to your question.",
            "the chariot":"I sense triumph and success over issues related to health or money.  Momentum is growing, but pay attention to where things are heading.",
            "strength":"I see courage and power, which could lead to overly assertive behavior.  Care must be taken to maintain a balance between opposing forces.",
            "the hermit":"I see prudence and discretion.  Be open to receive instruction from an expert in the search for knowledge.",
            "the wheel of fortune":"There may be success, unexpected change in luck or fortune for the better.  Take advantage of new opportunities.",
            "justice":"Balance is required. Eliminate excess baggage, wrong ideas, and useless forms of education.  Look for a mixture of the right ingredients.",
            "the hanged man":"You may want to suspend decisions.  Sacrifices may need to be made.",
            "death":"Let go and accept change.  There will be transformation, change, and destruction followed by new opportunities.",
            "temperance":"Learn to transfer your energy from the imagination to realization.  Adaptation is an important component.",
            "the devil":"I sense discontent, depression and illness.  Be aware of destructive tendencies.",
            "the tower":"There is change, conflict, and catastrophe surrounding the subject.  Disruption will bring enlightenment, however.",
            "the star":"There is insight, inspiration, hope and dreams.  There is a light at the end of the tunnel.",
            "the moon":"I sense some deception, or hidden factors.  There may be confusion and uncertainty.",
            "the sun":"It looks like there may be material happiness, success, liberation, gratitude and attainment.  There are achievements in work and school.",
            "judgment":"I see a life well lived, and work well done.  There is an awakening, along with accountability.",
            "the world":"I see fulfillment, gain, or achievement of something worked for or deserved.  Completion, reward, and success are near.",
            "ace of wands":"I see the beginning of a journey, an adventure, or an escapade.",
            "two of wands":"The answer lies with a new idea or an opportunity.",
            "three of wands":"Realization of hope, established strength, wealth and power.  There may be a partnership involved.",
            "four of wands":"Hard work, persistence, peace, prosperity, and harmony.",
            "five of wands":"Uh oh.  There is violent strife and competition.  You may be facing obstacles or limitations that will hold back progress.",
            "six of wands":"There is good news.  Advancement in work, and your friends may be helpful.",
            "seven of wands":"I sense tiredness and a lack of motivation for key projects.",
            "eight of wands":"There is a renewed fire and spirit.  There is movement in the air, but it may be too fast.",
            "nine of wands":"I sense exhaustion.  There will be a pause in your struggle.  There will be eventual victory, but a steady force must be applied.",
            "ten of wands":"There is a force and energy being applied, but power is unwisely used.  You are taking on too much.",
            "page of wands":"I sense passion around a creative idea, but it needs some refinement.",
            "knight of wands":"I sense impulsiveness, and perhaps a change of residence, emigration, or a quick departure.",
            "queen of wands":"I sense upcoming success in your endeavors, and loyalty, generosity and kindness.",
            "king of wands":"I sense honesty, friendliness, and passion.  A leader in a position of authority, who is happy when facing challenges.",
            "ace of cups":"I sense relationships unfolding, desire for companionship",
            "two of cups":"I see partnerships and the development of a bond",
            "three of cups":"There may be a celebration of something special coming soon.",
            "four of cups":"I sense indifference.  The subject is slightly disengaged from the activity.",
            "five of cups":"Be prepared to be upset or disappointed with the situation.",
            "six of cups":"Be careful not to take a trip down memory lane.  I sense regret.",
            "seven of cups":"There are so many decisions to make!",
            "eight of cups":"Be prepared for separation, heartbreak, and lost hope.",
            "nine of cups":"I sense a meaningful relationship or engagement.  There are happy times ahead.",
            "ten of cups":"There are strong bonds, a strong family connection, and emotional contentment.",
            "page of cups":"I sense inconsistencies.  There seems to be a swing between being studious and giving into daydreaming.",
            "knight of cups":"You may receive a message, a proposition, or an invitation.",
            "queen of cups":"I sense honesty, devotion, and loyalty.  There may be success and happiness in the future.",
            "king of cups":"The subject may not be as in touch with their emotions as you might think.",
            "ace of swords":"There are challenges ahead, as you may be faced with a change in belief.",
            "two of swords":"You may be avoiding conflict that needs to be faced or talked about.",
            "three of swords":"I sense a betrayal or loss.  There may be disappointment, separation, or quarreling.",
            "four of swords":"This is a time for contemplation and recuperation.",
            "five of swords":"I sense failure, defeat, cruelty and cowardliness.",
            "six of swords":"There may be a calm moment in an otherwise difficult situation.",
            "seven of swords":"Be alert.  There is the potential for deception or dishonesty.",
            "eight of swords":"I sense that the subject is being driven by fear, and there may be betrayal.",
            "nine of swords":"There may be suffering, loss, doubt.  A fresh mental perspective may be needed.",
            "ten of swords":"Your plans or projects will be ruined.  Tears will fall.  There will be a biter and difficult ending.",
            "page of swords":"Be wary of childish behavior.",
            "knight of swords":"There is misfortune in the air.",
            "queen of swords":"A guarded but intelligent woman may be involved.",
            "king of swords":"I sense power, strength, and authority.  There may be wise counsel given.",
            "ace of pentacles":"I sense the beginning of wealth and material gain.",
            "two of pentacles":"I sense a feeling of lightheartedness.  There is harmony in the midst of change.",
            "three of pentacles":"Be prepared to celebrate success or material gain.",
            "four of pentacles":"There may be gifts, material gain, or success.  Avoid risk or challenge.",
            "five of pentacles":"I sense financial and security issues that will cause concern. Perhaps the subject involves someone who will be facing unemployment or loneliness.",
            "six of pentacles":"The subject may involve the receipt of a gift, bonus, or loan.  There may be some positive feelings about people and the future.",
            "seven of pentacles":"I sense someone who may be feeling insecure on some level.  They may need to make a decision about their future.",
            "eight of pentacles":"I sense someone who is learning a trade or profession, and employment or a commission is in their future.",
            "nine of pentacles":"I sense someone who will reap the rewards of hard work and commitment.  This is a time for them to feel proud.",
            "ten of pentacles":"I sense strong bonds and a solid foundation.  Someone who seem to have a happy, fulfilled, and secure lifestyle.",
            "page of pentacles":"I sense a person who is searching for help on a project, but also has a lot to learn.",
            "knight of pentacles":"I sense a person who is responsible, and is a creature of habit that enjoys routine.",
            "queen of pentacles":"I sense a person who is self-sufficient and has achieved a lot.  They have earned the trust of those around them.",
            "king of pentacles":"I sense a person who does not like to take risks.  They are trustworthy, kind, and reliable.  They have a steady temperament."
        }
        
        res = "None"
        if card in cardDic:
            res = cardDic[card]
        #attributes_manager = handler_input.attributes_manager
        #card_attributes = {
        #    "card": card,
        #}
        #attributes_manager.persistent_attributes = card_attributes
        #attributes_manager.save_persistent_attributes()
        speak_output = '{res}'.format(res=res)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Draw six cards and read the names to me"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()
#CustomSkillBuilder(persistence_adapter=s3_adapter)


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureTarotIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
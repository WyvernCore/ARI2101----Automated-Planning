(define (domain slidingtilepuzzle)
    (:requirements :typing)
    
    (:types location locatable - object
            tile - locatable)
    
    (:predicates
            (at ?t - tile ?loc - location)
            (leftof ?loc1 ?loc2 - location)
            (rightof ?loc1 ?loc2 - location)
            (topof ?loc1 ?loc2 - location)
            (bottomof ?loc1 ?loc2 - location)
            (empty ?loc - location))
    
    (:action SLIDE-LEFT
        :parameters
        (?t - tile
         ?cLoc ?nLoc - location)
        :precondition
        (and (at ?t ?cLoc) (empty ?nLoc) (rightof ?cLoc ?nLoc) (leftof ?nLoc ?cLoc))
        :effect
        (and (not (at ?t ?cLoc)) (at ?t ?nLoc) (empty ?cLoc) (not (empty ?nLoc)))
    )
    
    (:action SLIDE-RIGHT
        :parameters
        (?t - tile
         ?cLoc ?nLoc - location)
        :precondition
        (and (at ?t ?cLoc) (empty ?nLoc) (leftof ?cLoc ?nLoc) (rightof ?nLoc ?cLoc))
        :effect
        (and (not (at ?t ?cLoc)) (at ?t ?nLoc) (empty ?cLoc) (not (empty ?nLoc)))
    )
    
    (:action SLIDE-UP
        :parameters
        (?t - tile
         ?cLoc ?nLoc - location)
        :precondition
        (and (at ?t ?cLoc) (empty ?nLoc) (bottomof ?cLoc ?nLoc) (topof ?nLoc ?cLoc))
        :effect
        (and (not (at ?t ?cLoc)) (at ?t ?nLoc) (empty ?cLoc) (not (empty ?nLoc)))
    )
    
    (:action SLIDE-DOWN
        :parameters
        (?t - tile
         ?cLoc ?nLoc - location)
        :precondition
        (and (at ?t ?cLoc) (empty ?nLoc) (topof ?cLoc ?nLoc) (bottomof ?nLoc ?cLoc))
        :effect
        (and (not (at ?t ?cLoc)) (at ?t ?nLoc) (empty ?cLoc) (not (empty ?nLoc)))
    )  
    
)
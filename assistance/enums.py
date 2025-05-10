from enum import Enum


class HelpTypeEnum(str, Enum):
    SHELTER = 'shelter'
    EVACUATION = 'evacuation'
    MEDICINE = 'medicine'
    FOOD = 'food'
    PSYCHOLOGICAL = 'psychological'
    CLOTHES = 'clothes'
    TRANSPORT = 'transport'
    INFO_SUPPORT = 'info_support'
    LEGAL = 'legal'
    REPAIR = 'repair'
    VOLUNTEER = 'volunteer'
    OTHER = 'other'


class HelpStatusEnum(str, Enum):
    OPEN = 'open'
    IN_PROGRESS = 'in_progress'
    RESOLVED = 'resolved'
    REJECTED = 'rejected'

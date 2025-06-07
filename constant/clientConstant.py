import mod.client.extraClientApi as clientApi

from .commonConstant import *

PLAYER_ID = clientApi.GetLocalPlayerId()
LEVEL_ID = clientApi.GetLevelId()
COMPONENT_FACTORY = clientApi.GetEngineCompFactory()

TimeComp = COMPONENT_FACTORY.CreateTime(LEVEL_ID)
TextNotifyComp = COMPONENT_FACTORY.CreateTextNotifyClient(LEVEL_ID)
ItemComp = COMPONENT_FACTORY.CreateItem(PLAYER_ID)
CustomAudioComp = COMPONENT_FACTORY.CreateCustomAudio(LEVEL_ID)
GameComp = COMPONENT_FACTORY.CreateGame(LEVEL_ID)
OperationComp = COMPONENT_FACTORY.CreateOperation(LEVEL_ID)
EngineTypeComp = COMPONENT_FACTORY.CreateEngineType
PosComp = COMPONENT_FACTORY.CreatePos(PLAYER_ID)
RotComp = COMPONENT_FACTORY.CreateRot(PLAYER_ID)

ENUM = clientApi.GetMinecraftEnum()

# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

from .commonConstant import *

LEVEL_ID = serverApi.GetLevelId()
COMPONENT_FACTORY = serverApi.GetEngineCompFactory()

HttpComp = COMPONENT_FACTORY.CreateHttp(LEVEL_ID)
CommandComp = COMPONENT_FACTORY.CreateCommand(LEVEL_ID)
MsgComp = COMPONENT_FACTORY.CreateMsg # 可传入LEVEL_ID和PLAYER_ID
TimeComp = COMPONENT_FACTORY.CreateTime(LEVEL_ID)
GameComp = COMPONENT_FACTORY.CreateGame(LEVEL_ID)
BlockComp = COMPONENT_FACTORY.CreateBlock(LEVEL_ID)
ItemComp = COMPONENT_FACTORY.CreateItem
NameComp = COMPONENT_FACTORY.CreateName
PosComp = COMPONENT_FACTORY.CreatePos
RotComp = COMPONENT_FACTORY.CreateRot
EffectComp = COMPONENT_FACTORY.CreateEffect
EntityDefinitionsComp = COMPONENT_FACTORY.CreateEntityDefinitions
PlayerComp = COMPONENT_FACTORY.CreatePlayer
TagComp = COMPONENT_FACTORY.CreateTag
EngineTypeComp = COMPONENT_FACTORY.CreateEngineType
DimensionComp = COMPONENT_FACTORY.CreateDimension

RunCommand = CommandComp.SetCommand

ENUM = serverApi.GetMinecraftEnum()




import bpy


class SOURCEOPS_UL_GameList(bpy.types.UIList):
    bl_idname = 'SOURCEOPS_UL_GameList'

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.prop(item, 'display', text='', emboss=False, translate=False)


class SOURCEOPS_UL_ModelList(bpy.types.UIList):
    bl_idname = 'SOURCEOPS_UL_ModelList'

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.prop(item, 'display', text='', emboss=False, translate=False)


class SOURCEOPS_UL_MaterialFolderList(bpy.types.UIList):
    bl_idname = 'SOURCEOPS_UL_MaterialFolderList'

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.prop(item, 'display', text='', emboss=False, translate=False)


class SOURCEOPS_UL_SequenceList(bpy.types.UIList):
    bl_idname = 'SOURCEOPS_UL_SequenceList'

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.prop(item, 'display', text='', emboss=False, translate=False)


class SOURCEOPS_UL_EventList(bpy.types.UIList):
    bl_idname = 'SOURCEOPS_UL_EventList'

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.prop(item, 'display', text='', emboss=False, translate=False)
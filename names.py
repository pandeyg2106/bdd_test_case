from objectmaphelper import *

application_window = {"type": "QQuickWindowQmlImpl", "title": "remarkable_mobile"}

# Top menu bar
topMenu_new_folder = {"container": application_window, "id": "newFolder", "type": "RMIconButton"}
topMenu_search = {"container": application_window, "id": "searchButton", "type": "RMIconButton"}
# After adding a document to a folder user has to go back to My Files by selecting back button. For this purpose I have
# added a new field as topMenu_back under the Top menbu bar
topMenu_back = {"container": application_window, "id": "backButton", "type": "RMIconButton"}

# Drawer objects (when long-pressing items)
drawer_copy = {"container": application_window, "text": "Duplicate", "type": "SidebarItem"}
drawer_move = {"container": application_window, "text": "Move", "type": "SidebarItem"}
drawer_rename = {"container": application_window, "text": "Rename", "type": "SidebarItem"}
drawer_favorite = {"container": application_window, "text": "Favorite", "type": "SidebarItem"}
drawer_send = {"container": application_window, "text": "Send", "type": "SidebarItem"}
drawer_move_to_trash = {"container": application_window, "text": "Move to trash", "type": "SidebarItem"}
drawer_delete = {"container": application_window, "text": "Delete", "type": "SidebarItem"}
drawer_restore = {"container": application_window, "text": "Restore", "type": "SidebarItem"}

# Header objects (when completing or cancelling action from a long-press)
header_close = {"container": application_window, "id": "closeButton","type": "RMIconButton"}
header_select_multiple = {"container": application_window, "id": "selectButton","type": "RMIconButton"}
header_confirm_selection = {"container": application_window, "id": "confirmSelectionButton", "type": "RMIconButton"}

# Move action buttons
movePanel_move = {"container": application_window, "id": "moveButton", "type": "NavigatorToolButton"}
movePanel_cancel_move = {"container": application_window, "id": "cancelMoveButton", "type": "NavigatorToolButton"}
movePanel_label = {"container": application_window, "id": "moveLabel", "type": "StyledText", "text": "Select a destination for your item"}

# Sidebar menu items
sidebar_my_files = {"container": application_window, "id": "filterMyFiles", "type": "SidebarFilterItem"}
sidebar_notebooks = {"container": application_window, "id": "filterNotebooks", "type": "SidebarFilterItem"}
sidebar_pdfs = {"container": application_window, "id": "filterDocuments", "type": "SidebarFilterItem"}
sidebar_ebooks = {"container": application_window, "id": "filterEbooks", "type": "SidebarFilterItem"}
sidebar_favorites = {"container": application_window, "id": "filterPinned", "type": "SidebarFilterItem"}
sidebar_trash = {"container": application_window, "id": "filterTrashed", "type": "SidebarFilterItem"}
sidebar_settings = {"container": application_window, "id": "settingsButton", "type": "SidebarFilterItem"}

# Layout styles
layout_GridView = {"container": application_window, "id": "gridView", "type": "GridView"}
layout_ListView = {"container": application_window, "id": "listView", "type": "ListView"}

# Search view
search_input_field = {"container": application_window, "id": "searchField", "type": "TextInput"}
search_results = {"container": application_window, "id": "searchGridView", "type": "EntryGridView"} 

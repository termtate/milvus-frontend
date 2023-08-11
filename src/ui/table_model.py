from typing import Any, Union
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt

from typing_extensions import override
from config import settings
from network.model import Patient

class TableModel(QAbstractTableModel):
    
    def __init__(self, data: list[Patient]):
        super(TableModel, self).__init__()
        self._data = data
        
    @override
    def data(
        self, 
        index: QModelIndex | QPersistentModelIndex, 
        role: int
    ) -> Any:
        match role:
            case Qt.ItemDataRole.DisplayRole:
                
        return super().data(index, role)
    
    @override
    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._data)

    @override
    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(settings.TABLE_COLUMNS)
    
    @override
    def headerData(self, section: int, orientation, role: int = ...) -> Any:
        match role:
            case Qt.ItemDataRole.DisplayRole:
                if orientation == Qt.Orientation.Horizontal:
                    return str(settings.TABLE_COLUMNS[section])
                # elif orientation == Qt.Orientation.Vertical:
                #     return str(self._data.index(se))
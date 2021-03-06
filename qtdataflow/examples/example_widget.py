__author__ = 'Tillsten'

from qtdataflow.view import WidgetNodeView, SchemaView
from qtdataflow.model import Node, Schema
from qtdataflow.Qt import QtGui
QSpinBox = QtGui.QSpinBox
QApplication = QtGui.QApplication
QGraphicsView = QtGui.QGraphicsView

class SpinBoxNode(Node):
    def __init__(self):
        super(SpinBoxNode, self).__init__()
        self.node_type = 'SpinBoxNode'
        self.generates_output = True
        self.sb = QSpinBox()
        self.sb.setGeometry(0,0,50,25)
        self.sb.valueChanged.connect(self.signal_change)

    def get_view(self):
        return WidgetNodeView(self)

    def get_widget(self):
        return self.sb

    def get(self):
        return self.sb.value()

    def signal_change(self):
        for n in self.out_conn:
            n.update()


class SumLabelNode(Node):
    def __init__(self):
        super(SumLabelNode, self).__init__()
        self.node_type = 'Sum Label'
        self.accepts_input = True
        self.lbl = QLabel()

    def get_view(self):
        return WidgetNodeView(self)

    def get_widget(self):
        return self.lbl

    def update(self):
        s = sum((n.get() for n in self.in_conn))
        self.lbl.setText(str(s))

if __name__ == '__main__':
    app = QApplication([])
    sch = Schema()
    sv = SchemaView(sch)
    n = SpinBoxNode()
    n2 = SpinBoxNode()
    n3 = SumLabelNode()
    sch.add_node(n)
    sch.add_node(n2)
    sch.add_node(n3)
    gv = QGraphicsView(sv)
    gv.show()

    app.exec_()
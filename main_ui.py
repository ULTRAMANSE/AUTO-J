# coding = utf-8
import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QStackedWidget, QAction, QStatusBar, QTableWidget,
							 QHBoxLayout, QHeaderView)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Main_ui(QMainWindow):
	def __init__(self, parent=None):
		super(Main_ui, self).__init__(parent)
		self.setFixedSize(1000, 700)
		self.setWindowTitle("AUTO-J V0.1")
		self.widget = QWidget()

		# 初始化
		self.set_statusbar()
		self.set_menu()
		self.set_layout()
		self.set_table_widget()

		# 设置stackedWidget
		self.stackedWidget = QStackedWidget()
		self.setCentralWidget(self.stackedWidget)
		self.stackedWidget.addWidget(self.widget)

	def set_menu(self):
		"""
		设置菜单工具栏
		:return:
		"""
		toolbar = self.addToolBar("工具栏")
		toolbar.setIconSize(QSize(50, 50))
		toolbar.setStyleSheet("QToolBar{spacing:10px;}")
		read_form = QAction(QIcon("./ico/读取.png"), "读取申请单", self)
		settings = QAction(QIcon("./ico/设置.png"), "设置", self)
		import_word = QAction(QIcon("./ico/填写.png"), "填写说明记录", self)
		change_flag = QAction(QIcon("./ico/转换.png"), "标识转换", self)
		sgin_in = QAction(QIcon("./ico/用户.png"), "用户登录", self)
		report = QAction(QIcon("./ico/生成报告.png"), "生成报告", self)

		toolbar.addAction(read_form)
		toolbar.addAction(change_flag)
		toolbar.addAction(import_word)
		toolbar.addAction(report)
		toolbar.addAction(sgin_in)
		toolbar.addAction(settings)

	def set_statusbar(self):
		"""
		设置状态栏
		:return:
		"""
		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)

	def set_layout(self):
		self.glayout = QHBoxLayout()
		self.widget.setLayout(self.glayout)

	def set_table_widget(self):
		"""
		设置列表
		:return:
		"""

		self.table_widget = QTableWidget(5, 8)
		# self.table_widget.setVerticalHeaderLabels()
		self.table_widget.setHorizontalHeaderLabels(["委托单编号", "项目编号", "软件名称", "版本", "委托方", "指派人", "执行人", "派单时间"])
		self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.table_widget.verticalHeader().setDisabled(True)  # 不改行高
		self.table_widget.setColumnWidth(3, 1)
		self.glayout.addWidget(self.table_widget)


if __name__ == '__main__':
	App = QApplication(sys.argv)
	ex = Main_ui()
	ex.show()
	sys.exit(App.exec_())

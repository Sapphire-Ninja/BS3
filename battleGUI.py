from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QMessageBox, QAction, QMenuBar, QMenu, QStatusBar
from classes.game import *


class Ui_BattleSimulatorWindow(object):

    def __init__(self, players, enemies):
        self.statusbar = QStatusBar(BattleSimulatorWindow)
        self.menubar = QMenuBar(BattleSimulatorWindow)
        self.menuFile = QMenu(self.menubar)
        self.actionWczytaj = QAction(BattleSimulatorWindow)
        self.actionZapisz = QAction(BattleSimulatorWindow)
        self.players = players
        self.enemies = enemies
        self.centralwidget = QtWidgets.QWidget(BattleSimulatorWindow)
        self.scroll_area_team = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.team_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.scroll_area_enemies = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.enemies_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.proceed_button = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_area_spells = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.spells_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.scroll_area_info = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.info_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scroll_area_items = QtWidgets.QScrollArea(self.centralwidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.items_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.combobox_action = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_selection = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_target = QtWidgets.QComboBox(self.centralwidget)

        self.num_players = len(self.players)
        self.turn = 1
        self.index = 0
        if self.num_players < 1:
            self.index = -1
        self.player = self.players[self.index]
        self.last_round_info = ""

    def setupUi(self, BattleSimulatorWindow):
        BattleSimulatorWindow.setObjectName("Battle Simulator III - swords and magic")
        BattleSimulatorWindow.setFixedSize(1200, 800)
        BattleSimulatorWindow.setMouseTracking(True)
        BattleSimulatorWindow.setTabletTracking(True)
        self.actionZapisz.setObjectName(u"actionZapisz")
        self.actionWczytaj.setObjectName(u"actionWczytaj")
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile.setObjectName(u"menuFile")
        BattleSimulatorWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName(u"statusbar")
        BattleSimulatorWindow.setStatusBar(self.statusbar)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        BattleSimulatorWindow.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.scroll_area_team.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.scroll_area_team.setWidgetResizable(True)
        self.scroll_area_team.setObjectName("scroll_area_team")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 398))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout.setObjectName("horizontalLayout")
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.team_label.setFont(font)
        self.team_label.setObjectName("team_label")
        self.horizontalLayout.addWidget(self.team_label)
        self.scroll_area_team.setWidget(self.scrollAreaWidgetContents)
        self.scroll_area_enemies.setGeometry(QtCore.QRect(600, 0, 600, 400))
        self.scroll_area_enemies.setWidgetResizable(True)
        self.scroll_area_enemies.setObjectName("scroll_area_enemies")
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 598, 398))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.enemies_label.setFont(font)
        self.enemies_label.setObjectName("enemies_label")
        self.horizontalLayout_2.addWidget(self.enemies_label)
        self.scroll_area_enemies.setWidget(self.scrollAreaWidgetContents_2)
        self.proceed_button.setGeometry(QtCore.QRect(900, 700, 300, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceed_button.sizePolicy().hasHeightForWidth())
        self.proceed_button.setSizePolicy(sizePolicy)
        self.proceed_button.setObjectName("proceed_button")
        self.scroll_area_spells.setGeometry(QtCore.QRect(0, 400, 400, 250))
        self.scroll_area_spells.setWidgetResizable(True)
        self.scroll_area_spells.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_area_spells.setObjectName("scroll_area_spells")
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 398, 248))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.spells_label.setFont(font)
        self.spells_label.setObjectName("spells_label")
        self.horizontalLayout_4.addWidget(self.spells_label)
        self.scroll_area_spells.setWidget(self.scrollAreaWidgetContents_4)
        self.scroll_area_info.setGeometry(QtCore.QRect(400, 400, 400, 250))
        self.scroll_area_info.setWidgetResizable(True)
        self.scroll_area_info.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_area_info.setObjectName("scroll_area_info")
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 398, 248))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.info_label.setFont(font)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.info_label.setWordWrap(True)
        self.horizontalLayout_5.addWidget(self.info_label)
        self.scroll_area_info.setWidget(self.scrollAreaWidgetContents_5)
        self.scroll_area_items.setGeometry(QtCore.QRect(790, 400, 400, 250))
        self.scroll_area_items.setWidgetResizable(True)
        self.scroll_area_items.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_area_items.setObjectName("scroll_area_items")
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 398, 248))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.items_label.setFont(font)
        self.items_label.setObjectName("items_label")
        self.horizontalLayout_6.addWidget(self.items_label)
        self.scroll_area_items.setWidget(self.scrollAreaWidgetContents_6)
        self.combobox_action.setGeometry(QtCore.QRect(0, 700, 300, 30))
        self.combobox_action.setObjectName("combobox_action")
        self.combobox_action.addItem("")
        self.combobox_action.addItem("")
        self.combobox_action.addItem("")
        self.combobox_action.addItem("")
        self.combobox_selection.setGeometry(QtCore.QRect(300, 700, 300, 30))
        self.combobox_selection.setObjectName("combobox_choose")
        self.combobox_selection.addItem("Choose")
        self.combobox_target.setGeometry(QtCore.QRect(600, 700, 300, 30))
        self.combobox_target.setObjectName("combobox_target")
        self.combobox_target.addItem("")
        BattleSimulatorWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        BattleSimulatorWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        BattleSimulatorWindow.setStatusBar(self.statusbar)
        self.scroll_area_team.setStyleSheet("background : lightyellow")
        self.scroll_area_enemies.setStyleSheet("background : lightyellow")
        self.scroll_area_info.setStyleSheet("background : lightyellow")
        self.scroll_area_spells.setStyleSheet("background-color : darkorange")
        self.scroll_area_items.setStyleSheet("background-color : limegreen")
        self.spells_label.setStyleSheet("background : orange")
        self.items_label.setStyleSheet("background : lightgreen")
        self.proceed_button.setStyleSheet("QPushButton { border-image : url(dataToLoad/images/plank.png);}"
                                          "QPushButton:hover { border-image : url(dataToLoad/images/light plank.png);}"
                                          "QPushButton:pressed { border-image : url(dataToLoad/images/dark plank.png);}")
        self.combobox_action.setStyleSheet("")

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionZapisz)
        self.menuFile.addAction(self.actionWczytaj)

        self.retranslateUi(BattleSimulatorWindow)
        QtCore.QMetaObject.connectSlotsByName(BattleSimulatorWindow)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionZapisz)
        self.menuFile.addAction(self.actionWczytaj)

        # changed stuff
        self.start_game()
        self.proceed_button.clicked.connect(self.popup_take_action)
        self.combobox_action.activated[str].connect(self.update_combo_selection)
        self.combobox_selection.activated[str].connect(self.update_combo_targets)
        self.actionZapisz.triggered.connect(lambda: self.save_status_to_file())
        self.actionWczytaj.triggered.connect(lambda: self.load_last_save())

    def retranslateUi(self, BattleSimulatorWindow):
        _translate = QtCore.QCoreApplication.translate
        BattleSimulatorWindow.setWindowTitle(_translate("BattleSimulatorWindow", "Battle Simulator III - "
                                                                                 "swords and magic"))
        self.actionZapisz.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        # if QT_CONFIG(shortcut)
        self.actionZapisz.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
        # endif // QT_CONFIG(shortcut)
        self.actionWczytaj.setText(QCoreApplication.translate("MainWindow", u"Wczytaj", None))
        # if QT_CONFIG(shortcut)
        self.actionWczytaj.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
        # endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.team_label.setText(_translate("BattleSimulatorWindow", "TextLabel"))
        self.enemies_label.setText(_translate("BattleSimulatorWindow", "TextLabel"))
        self.proceed_button.setText(_translate("BattleSimulatorWindow", "Take Action"))
        self.spells_label.setText(_translate("BattleSimulatorWindow", "TextLabel"))
        self.info_label.setText(_translate("BattleSimulatorWindow", "TextLabel"))
        self.items_label.setText(_translate("BattleSimulatorWindow", "TextLabel"))
        self.combobox_action.setItemText(0, _translate("BattleSimulatorWindow", "Action"))
        self.combobox_action.setItemText(1, _translate("BattleSimulatorWindow", "Attack"))
        self.combobox_action.setItemText(2, _translate("BattleSimulatorWindow", "Cast spell"))
        self.combobox_action.setItemText(3, _translate("BattleSimulatorWindow", "Use Item"))
        self.combobox_target.setItemText(0, _translate("BattleSimulatorWindow", "Target"))

    def update_player(self):
        self.player = self.players[self.index]
        if self.player.get_hp() == 0:
            self.last_round_info += "\nDue to " + self.player.name + "'s death, he is unable to move."
            self.next_player()

    def update_label_stats(self):

        self.enemies_label.setText("<font color='black'><pre class='tab'>============= ENEMIES ==============<br>" +
                                   "<br>".join([
                                       foe.get_stats()[0] + ":<br>HP: " + foe.get_stats()[1] +
                                       "<br>|<font color=\'firebrick\'>" + foe.get_stats()[2] +
                                       "<font color='black'>|<br>"
                                       for foe in self.enemies
                                   ]) + "</pre></font>")

        self.team_label.setText("<font color='black'><pre class='tab'>============= TEAMMATES ==============<br>" +
                                "<br>".join([
                                    guy.get_stats()[0] + ":<br>HP:  " + guy.get_stats()[1] +
                                    "<br>|<font color=\'seagreen\'>" + guy.get_stats()[2] +
                                    "<font color='black'>|<br>MP:  " + guy.get_stats()[3] +
                                    "<br>|<font color=\'blue\'>" + guy.get_stats()[4] + "<font color='black'>|<br>"
                                    for guy in self.players
                                ]) + "</pre></font>")

    def update_label_info(self):
        dead_enemies = 0
        for e in self.enemies:
            if e.get_hp() == 0:
                dead_enemies += 1

        if dead_enemies == len(self.enemies):
            self.info_label.setText("<pre class='tab'>!!!YOU WON!!!</pre>")

        else:
            string_turn = "============== TURN " + str(self.turn) + " ==============\n\n"
            string_turn += self.last_round_info + "\n\n"
            string_turn += self.player.name + "\nAbility Power: " + str(self.player.ap * 100) + \
                           "\nAttack Damage: " + str(self.player.attack)
            self.info_label.setText(string_turn)

    def update_label_spells(self):
        string_spells = self.player.spells_toString()
        self.spells_label.setText(string_spells)

    def update_label_items(self):
        string_items = self.player.items_toString()
        self.items_label.setText(string_items)

    def update_combo_targets(self):
        self.combobox_target.clear()
        self.combobox_target.addItem("Choose target")

        if self.combobox_action.currentText() == "Cast spell" and self.player.magic:
            index_selection_box = self.combobox_selection.currentIndex() - 1
            spell = self.player.magic[index_selection_box]

            if spell.aoe:
                self.combobox_target.addItem("EVERYONE")

            elif spell.nature == "light":
                for player in self.players:
                    self.combobox_target.addItem(player.name)

            else:
                for foe in self.enemies:
                    if foe.get_hp() > 0:
                        self.combobox_target.addItem(foe.name)

        elif self.combobox_action.currentText() == "Use Item" and self.player.items:
            index_selection_box = self.combobox_selection.currentIndex() - 1
            item = self.player.items[index_selection_box]["item"]

            if item.aoe:
                self.combobox_target.addItem("EVERYONE")

            elif item.category == "healing" or item.category == "mana" or item.category == "elixir":
                for player in self.players:
                    self.combobox_target.addItem(player.name)

            else:
                for foe in self.enemies:
                    if foe.get_hp() > 0:
                        self.combobox_target.addItem(foe.name)

        else:
            for foe in self.enemies:
                if foe.get_hp() > 0:
                    self.combobox_target.addItem(foe.name)

    def update_combo_selection(self, text):
        self.combobox_selection.clear()
        self.update_combo_targets()
        self.combobox_selection.addItem("Choose")

        if text == "Attack":
            self.combobox_selection.addItem("Slash!")
            self.combobox_selection.addItem("Stab!")

        elif text == "Cast spell":
            if self.player.magic:
                for spell in self.player.magic:
                    self.combobox_selection.addItem(spell.name)
            else:
                self.combobox_selection.addItem("You dont have any spells :(")
                self.reset_combos()

        elif text == "Use Item":
            if self.player.items:
                for item in self.player.items:
                    if item["quantity"] > 0:
                        self.combobox_selection.addItem(item["item"].name)
            else:
                self.combobox_selection.addItem("You dont have any items :(")
                self.reset_combos()

    def reset_combos(self):
        self.combobox_action.setCurrentIndex(0)
        self.combobox_target.setCurrentIndex(0)
        self.combobox_selection.setCurrentIndex(0)
        self.update_combo_targets()

    def start_game(self):
        self.update_label_stats()
        self.update_label_spells()
        self.update_label_info()
        self.update_label_items()
        self.update_combo_targets()

    def next_player(self):
        self.index += 1
        if self.index >= self.num_players:
            self.last_round_info += monsters_attack(self.players, self.enemies)
            self.index = self.index % self.num_players
            self.turn += 1
        self.update_player()
        self.update_label_stats()
        self.update_label_info()
        self.update_label_spells()
        self.update_label_items()
        self.reset_combos()

    def popup_take_action(self):
        msg = QMessageBox()
        msg.setWindowTitle("Action Menu")
        msg.setText("Proceed to next turn?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)

        returned_value = msg.exec_()

        if returned_value == QMessageBox.Yes:
            if self.combobox_action.currentText() == "Action" or self.combobox_selection.currentText() == "Choose":
                err = QMessageBox()
                err.setWindowTitle("Are You sure?")
                err.setText("Exact Action hasn't been selected, do you want to give up your turn?")
                err.setIcon(QMessageBox.Critical)
                err.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

                answer = err.exec_()
                if answer == QMessageBox.Yes:
                    self.take_action()
            else:
                self.take_action()

    def take_action(self):
        selected_target = self.combobox_target.currentText()
        index_selection_box = self.combobox_selection.currentIndex() - 1
        index = 0
        counter = 0
        for foe in self.enemies:
            if foe.name == selected_target:
                index = counter
            counter += 1

        if self.combobox_action.currentText() == "Attack":
            damage = math.ceil(self.player.get_attack_damage())

            defender = self.enemies[index]
            if selected_target == "Action":
                defender = self.enemies[random.randrange(0, len(self.enemies))]
            defender.take_damage(damage, "force")
            self.last_round_info = self.player.name + " dealt about " + str(
                damage) + " force damage to " + defender.name

        elif self.combobox_action.currentText() == "Cast spell":
            spell = self.player.magic[index_selection_box]

            if spell.cost > self.player.get_mp():
                err = QMessageBox()
                err.setWindowTitle("You failed!")
                err.setText("You didnt have enough mana to cast this spell. Current MP: " + str(self.player.get_mp()) +
                            " Required: " + spell.cost + ". Next time better watch your stats!")
                err.setIcon(QMessageBox.Critical)
                answer = err.exec_()
                self.reset_combos()

            else:
                damage = math.ceil(self.player.get_spell_damage(spell))

                if spell.nature == "light":
                    counter = 0
                    for player in self.players:
                        if player.name == selected_target:
                            index = counter
                        counter += 1

                    healed = self.players[index]
                    healed.heal(damage)
                    self.last_round_info = self.player.name + " healed " + healed.name + " for " + str(damage) + \
                                           ", using " + spell.name

                elif spell.aoe:
                    for foe in self.enemies:
                        foe.take_damage(damage, spell.nature)
                        self.last_round_info = self.player.name + " dealt about " + str(damage) + " " + spell.nature \
                                               + " damage to EVERYONE, using " + spell.name

                else:
                    defender = self.enemies[index]
                    defender.take_damage(damage, spell.nature)
                    self.last_round_info = self.player.name + " dealt " + str(damage) + " " + spell.nature + \
                                           " damage to " + defender.name + ", using " + spell.name

                self.player.take_mana(spell.cost)

        elif self.combobox_action.currentText() == "Use Item":
            item_dex = 0
            counter = 0
            for item in self.player.items:
                if item["item"].name == selected_target:
                    item_dex = counter
                counter += 1

            item = self.player.items[item_dex]["item"]

            if item.category == "healing":
                counter = 0
                for player in self.players:
                    if player.name == selected_target:
                        index = counter
                    counter += 1

                healed = self.players[index]
                healed.heal(item.prop)
                self.last_round_info = self.player.name + " healed " + healed.name + " for " + str(item.prop) + \
                                       ", using " + item.name

            elif item.category == "elixir":
                counter = 0
                for player in self.players:
                    if player.name == selected_target:
                        index = counter
                    counter += 1

                healed = self.players[index]
                healed.heal(item.prop)
                healed.restore_mp(item.prop)
                self.last_round_info = self.player.name + " healed and restored mana of " + healed.name + " for " + \
                                       str(item.prop) + ", using " + item.name

            elif item.category == "attack" and item.aoe:
                damage = item.prop
                for foe in self.enemies:
                    foe.take_damage(damage, "force")
                    self.last_round_info = self.player.name + " dealt about " + str(damage) + \
                                           " damage to EVERYONE, using " + item.name

            elif item.category == "attack":
                damage = item.prop
                defender = self.enemies[index]
                defender.take_damage(damage, "force")

                self.last_round_info = self.player.name + " dealt " + str(damage) + " damage to " + \
                                       defender.name + " using " + item.name

            elif item.category == "mana":
                counter = 0
                for player in self.players:
                    if player.name == selected_target:
                        index = counter
                    counter += 1
                restored = self.players[index]
                restored.restore_mp(item.prop)
                self.last_round_info = self.player.name + " restored " + str(item.prop) + " MP to " + \
                                       restored.name + " using " + item.name

            self.player.items[index_selection_box]["quantity"] -= 1
        self.next_player()

    def save_status_to_file(self):
        f = open("save.txt", 'a', encoding='utf-8')
        f.truncate(0)
        f.write("Index: " + str(self.index) + "\tTurn: " + str(self.turn))
        f.write("\nPlayers\n")

        for player in players:
            to_save = player.save_player()
            f.write(to_save)
            f.write("\n")
        f.write("\nEnemies\n")

        for enemy in enemies:
            to_save = enemy.save_monster()
            f.write(to_save)
            f.write("\n")
        f.write("\nItems\n")

        for item in self.player.items:
            to_save = item["item"].save_item() + "\tQuantity: " + str(item["quantity"])
            f.write(to_save)
            f.write("\n")

        f.write("\nEnd")
        f.close()

    def load_last_save(self):
        f = open("save.txt", 'r', encoding='utf-8')
        self.players.clear()
        self.enemies.clear()
        list_lines = []
        itms = []

        for line in f:
            splitted_line = line.split()
            list_lines.append(splitted_line)

        f.close()

        if list_lines[0][0] == "Index:" and list_lines[0][1].isdigit():
            self.index = int(list_lines[0][1]) - 1
            if list_lines[0][2] == "Turn:" and list_lines[0][3].isdigit():
                self.turn = int(list_lines[0][3])

        i = 2
        if list_lines[1][0] == "Players":
            last_player = 0
            while list_lines[i]:
                temp = list_lines[i]
                if temp[0] == "Player:":
                    new_player = Person(temp[1], int(temp[2]), int(temp[4]), int(temp[6]), int(temp[7]), float(temp[8]), [])
                    new_player.hp = int(temp[3])
                    new_player.mp = int(temp[5])
                    self.players.append(new_player)
                    last_player += 1
                else:
                    new_spell = Spell(temp[0], int(temp[1]), int(temp[2]), temp[3], bool(temp[4]))
                    self.players[last_player - 1].magic.append(new_spell)

                i += 1
        i += 1
        if list_lines[i][0] == "Enemies":
            i += 1
            while list_lines[i]:
                temp = list_lines[i]
                if temp[0] == "Monster:":
                    new_monster = Monster(temp[1], int(temp[2]), int(temp[4]), int(temp[5]), int(temp[6]), temp[7])
                    new_monster.hp = int(temp[3])
                    self.enemies.append(new_monster)
                i += 1

        i += 1
        if list_lines[i][0] == "Items":
            i += 1
            while list_lines[i]:
                temp = list_lines[i]
                if temp[0] == "Item:":
                    new_item = Item(temp[1], temp[2], int(temp[3]), bool(temp[4]))
                    itms.append({"item": new_item, "quantity": int(temp[6])})
                    i += 1
                if temp[0] == "End":
                    break
            for player in self.players:
                player.items = itms
        self.next_player()


if __name__ == "__main__":
    import sys

    loaded = load_data()
    all_items = loaded[0]
    all_spells = loaded[1]
    all_monsters = loaded[2]

    num_of_items = random.randrange(0, len(all_items))
    player_items = random.sample(all_items, num_of_items)

    # PCs
    pc1 = Person("Bob", 200, 100, 15, 5, 0.95, player_items)
    pc2 = Person("Valos", 150, 100, 80, 10, 0.50, player_items)
    pc3 = Person("Harry", 400, 20, 85, 30, 0, player_items)

    players = [pc1, pc2, pc3]
    for p in players:
        p.generate_spell_book(all_spells)

    enemies = random.choices(all_monsters, k=6)

    app = QtWidgets.QApplication(sys.argv)
    BattleSimulatorWindow = QtWidgets.QMainWindow()
    ui = Ui_BattleSimulatorWindow(players, enemies)
    ui.setupUi(BattleSimulatorWindow)
    BattleSimulatorWindow.show()
    sys.exit(app.exec_())

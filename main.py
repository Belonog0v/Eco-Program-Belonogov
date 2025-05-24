from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QLineEdit, QComboBox, QDialog, QVBoxLayout, QTextEdit, QFileDialog,
                             QWidget, QMessageBox, QHBoxLayout, QTableWidget, QTableWidgetItem, QScrollArea,
                             QGroupBox, QButtonGroup, QRadioButton)
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, QPolygon, QBrush
from PyQt5.QtCore import Qt, QPoint, QRectF, QPointF
from math import pi, pow, sqrt
import math


class MainWindow(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Экономический ущерб атмосферному воздуху от выбросов загрязняющих веществ стационарным источником")
        self.setGeometry(100, 100, 800, 450)

        self.label = QLabel("Выберите тип загрязняемой местности", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 20, self.width(), 50)
        self.label.setStyleSheet("font-size: 30px; font-weight: bold;")

        self.button1 = QPushButton("Однородный", self)
        self.button1.setFixedSize(200, 50)
        self.button1.clicked.connect(self.open_homogeneous_window)
        self.button1.move(100, 100)

        self.button2 = QPushButton("Неоднородный", self)
        self.button2.setFixedSize(200, 50)
        self.button2.clicked.connect(self.open_heterogeneous_window)
        self.button2.move(500, 100)

    def open_homogeneous_window(self):
        self.new_window = FirstHomogeneousWindow(self)
        self.new_window.show()
        self.close()

    def open_heterogeneous_window(self):
        self.new_window = FirstHeterogeneousWindow(self)
        self.new_window.show()
        self.close()


class FirstHomogeneousWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.selected_terrain_type = None
        self.terrain_hazard_values = {
            "Территории курортов, заповедников, заказников": 10,
            "Территории природных зон отдыха и садовых участков, парков": 8,
            "Территория населенных пунктов с плотностью населения n чел/га": 10,
            "Территория населенных пунктов с плотностью более 300 чел./га": 8,
            "Территории промышленных предприятий (включая санитарно-защитную зону)": 4,
            "Леса: 1-я группа": 0.2,
            "Леса: 2-я группа": 0.1,
            "Леса: 3-я группа": 0.025,
            "Пашни: Южные зоны (южнее 50 гр. Северной широты)": 0.25,
            "Пашни: Центральный черноземный район, южная Сибирь": 0.15,
            "Пашни: Прочие районы": 0.1,
            "Сады, виноградники": 0.5,
            "Пастбища, сенокосы": 0.05
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Однородный тип местности")
        self.setGeometry(100, 100, 850, 750)

        # Левая колонка (поля ввода)
        y_pos = 50
        self.name_pollutant_input = QLineEdit(self)
        self.name_pollutant_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.average_PDK_input = QLineEdit(self)
        self.average_PDK_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.max_PLD_input = QLineEdit(self)
        self.max_PLD_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.ejection_mass_input = QLineEdit(self)
        self.ejection_mass_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.height_of_emission_input = QLineEdit(self)
        self.height_of_emission_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.emission_clean_factor_input = QLineEdit(self)
        self.emission_clean_factor_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.temperature_mixture_input = QLineEdit(self)
        self.temperature_mixture_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.average_temperature_input = QLineEdit(self)
        self.average_temperature_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.average_wind_input = QLineEdit(self)
        self.average_wind_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.const_to_rubles_input = QLineEdit(self)
        self.const_to_rubles_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50
        
        self.deflator_input = QLineEdit(self)
        self.deflator_input.setGeometry(50, y_pos, 300, 30)
        y_pos += 50

        # Правая колонка (подписи)
        y_pos = 50
        self.name_label = QLabel("Наименование загрязняющего вещества", self)
        self.name_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.average_PDK_label = QLabel("ПДК среднесуточная, мг/м3", self)
        self.average_PDK_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.max_PDK_label = QLabel("ПДК максимально-разовая, мг/м3", self)
        self.max_PDK_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.ejection_mass_label = QLabel("Масса валового выброса (m), т/год", self)
        self.ejection_mass_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.height_of_emission_label = QLabel("Высота стационарного источника выбросов (H), м", self)
        self.height_of_emission_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.emission_clean_factor_label = QLabel("Эффективность очистки выбросов, %", self)
        self.emission_clean_factor_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.temperature_mixture_label = QLabel("Температура выброса, Сº", self)
        self.temperature_mixture_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.average_temperature_label = QLabel("Среднегодовая температура атмосферного воздуха, Сº", self)
        self.average_temperature_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.average_wind_label = QLabel("Среднегодовая сила ветра (U), м/с", self)
        self.average_wind_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.const_to_rubles_label = QLabel("Удельный экономический ущерб от выбросов\nусловной тонны загрязняющего вещества, руб. усл/т", self)
        self.const_to_rubles_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50
        
        self.deflator_label = QLabel("Коэффициент-дефлятор", self)
        self.deflator_label.setGeometry(375, y_pos, 400, 30)
        y_pos += 50

        # Большая кнопка выбора типа местности
        self.terrain_type_button = QPushButton("Указать тип загрязняемой местности", self)
        self.terrain_type_button.setGeometry(50, y_pos, 750, 50)
        self.terrain_type_button.setStyleSheet("font-size: 14px;")
        self.terrain_type_button.clicked.connect(self.show_terrain_type_dialog)

        # Кнопки внизу окна
        button_y = 650
        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(200, 50)
        self.back_button.clicked.connect(self.close_first_homogeneous_window)
        self.back_button.move(50, button_y)

        self.save_button = QPushButton("Далее", self)
        self.save_button.setFixedSize(200, 50)
        self.save_button.clicked.connect(self.validate_and_save)
        self.save_button.move(600, button_y)

    def show_terrain_type_dialog(self):
        """Показывает диалоговое окно для выбора типа местности"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Выбор типа местности и коэффициента опасности")
        dialog.setFixedSize(800, 600)
        
        scroll = QScrollArea(dialog)
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        
        group_box = QGroupBox("Выберите тип местности:", dialog)
        group_layout = QVBoxLayout()
        
        self.terrain_button_group = QButtonGroup(dialog)
        
        for i, (terrain, value) in enumerate(self.terrain_hazard_values.items()):
            radio = QRadioButton(f"{terrain} (коэффициент опасности: {value})", dialog)
            radio.setStyleSheet("font-size: 12px; padding: 5px;")
            self.terrain_button_group.addButton(radio, i)
            group_layout.addWidget(radio)
        
        group_box.setLayout(group_layout)
        layout.addWidget(group_box)
        
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        
        confirm_button = QPushButton("Подтвердить выбор", dialog)
        confirm_button.setFixedSize(200, 40)
        confirm_button.clicked.connect(lambda: self.set_terrain_type(dialog))
        
        cancel_button = QPushButton("Отмена", dialog)
        cancel_button.setFixedSize(200, 40)
        cancel_button.clicked.connect(dialog.close)
        
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(cancel_button)
        layout.addWidget(button_container)
        
        scroll.setWidget(content)
        dialog_layout = QVBoxLayout(dialog)
        dialog_layout.addWidget(scroll)
        
        dialog.exec_()
    
    def set_terrain_type(self, dialog):
        """Устанавливает выбранный тип местности"""
        selected_button = self.terrain_button_group.checkedButton()
        if selected_button:
            terrain_text = selected_button.text().split(" (коэффициент опасности: ")[0]
            self.selected_terrain_type = terrain_text
            
            hazard_value = self.terrain_hazard_values[terrain_text]
            self.terrain_type_button.setText(
                f"Выбрано: {terrain_text} (коэффициент опасности: {hazard_value})"
            )
            self.terrain_type_button.setStyleSheet(
                "font-size: 14px; background-color: #e6f7ff;"
            )
            
            dialog.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите тип местности")

    def validate_and_save(self):
        """Проверяем данные перед сохранением"""
        if not self.selected_terrain_type:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, укажите тип загрязняемой местности")
            return
            
        fields = [
            ('pollutant_name', self.name_pollutant_input, False),
            ('average_PDK', self.average_PDK_input, True),
            ('max_PDK', self.max_PLD_input, True),
            ('ejection_mass', self.ejection_mass_input, True),
            ('height_of_emission', self.height_of_emission_input, True),
            ('emission_clean_factor', self.emission_clean_factor_input, True),
            ('temperature_mixture', self.temperature_mixture_input, True),
            ('average_temperature', self.average_temperature_input, True),
            ('average_wind', self.average_wind_input, True),
            ('const_to_rubles', self.const_to_rubles_input, True),
            ('deflator', self.deflator_input, True)
        ]
        
        data = {}
        errors = []
        
        for name, field, is_numeric in fields:
            value = field.text().strip()
            
            if not value:
                errors.append(f"Поле '{name}' не заполнено")
                continue
                
            if is_numeric:
                value = value.replace(',', '.')
                try:
                    float(value)
                except ValueError:
                    errors.append(f"Поле '{name}' должно содержать число")
                    continue
                    
            data[name] = value
        
        if errors:
            QMessageBox.warning(
                self, 
                "Ошибки ввода", 
                "Обнаружены следующие ошибки:\n\n• " + "\n• ".join(errors)
            )
            return
            
        data['terrain_type'] = self.selected_terrain_type
        data['hazard_index'] = self.terrain_hazard_values[self.selected_terrain_type]
        
        self.save_data(data)

    def save_data(self, data):
        """Сохранение данных и переход к следующему окну"""
        numeric_fields = [
            'average_PDK', 'max_PDK', 'ejection_mass', 
            'height_of_emission', 'emission_clean_factor',
            'temperature_mixture', 'average_temperature',
            'average_wind', 'const_to_rubles', 'deflator'
        ]
        
        processed_data = {}
        for key, value in data.items():
            if key in numeric_fields:
                processed_data[key] = float(value.replace(',', '.'))
            else:
                processed_data[key] = value
        
        # Сохраняем все данные, включая тип местности и коэффициент опасности
        processed_data.update({
            'terrain_type': self.selected_terrain_type,
            'hazard_index': self.terrain_hazard_values[self.selected_terrain_type]
        })
        
        self.second_window = SecondHomogeneousWindow(processed_data)
        self.second_window.show()
        self.close()

    def close_first_homogeneous_window(self):
        """Закрывает окно без сохранения данных"""
        self.close()
        self.main_window.show()


class SecondHomogeneousWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.selected_image_path = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Однородный тип местности")
        self.setGeometry(100, 100, 800, 720)

        # C 
        self.info_c_label = QLabel(
            "c – поправка, учитывающая вероятность накопления исходной примеси или вторичных загрязнителей в компонентах окружающей среды и цепях питания, "
            "а также поступления примеси в организм человека неингаляционным путем.",
            self
        )
        self.info_c_label.setGeometry(50, 20, 700, 60)
        self.info_c_label.setWordWrap(True)
        self.c_label = QLabel("Выберите поправку (c):", self)
        self.c_label.setGeometry(50, 90, 300, 30)
        self.c_combo = QComboBox(self)
        self.c_combo.setGeometry(225, 90, 400, 30)
        self.c_combo.addItems(["5", "2", "1"])

        self.explain_c_button = QPushButton("?", self)
        self.explain_c_button.setFixedSize(50, 50)
        self.explain_c_button.clicked.connect(self.show_explain_c_value)
        self.explain_c_button.move(650, 75)

        # delta
        self.info_delta_label = QLabel(
            "δ – поправка, характеризующая вредное воздействие примеси на реципиентов (за исключением человека)",
            self
        )
        self.info_delta_label.setGeometry(50, 120, 700, 60)
        self.info_delta_label.setWordWrap(True)
        self.delta_label = QLabel("Выберите поправку (δ)", self)
        self.delta_label.setGeometry(50, 180, 300, 30)
        self.delta_combo = QComboBox(self)
        self.delta_combo.setGeometry(225, 180, 400, 30)
        self.delta_combo.addItems(["2", "1.5", "1.2", "1"])

        self.explain_delta_button = QPushButton("?", self)
        self.explain_delta_button.setFixedSize(50, 50)
        self.explain_delta_button.clicked.connect(self.show_explain_delta_value)
        self.explain_delta_button.move(650, 170)

        # Lambda
        self.info_lambda_label = QLabel(
            'λ – поправка на вероятность вторичного заброса примесей в атмосферный воздух после их оседания на поверхностях.',
            self
        )
        self.info_lambda_label.setGeometry(50, 220, 700, 60)
        self.info_lambda_label.setWordWrap(True)
        self.lambda_label = QLabel("Выберите поправку (λ)", self)
        self.lambda_label.setGeometry(50, 270, 300, 30)
        self.lambda_combo = QComboBox(self)
        self.lambda_combo.setGeometry(225, 270, 400, 30)
        self.lambda_combo.addItems(["1.2", "1"])

        self.explain_lambda_button = QPushButton("?", self)
        self.explain_lambda_button.setFixedSize(50, 50)
        self.explain_lambda_button.clicked.connect(self.show_explain_lambda_value)
        self.explain_lambda_button.move(650, 265)

        self.info_beta_label = QLabel(
            'β – поправка на вероятность образования из исходных примесей, выброшенных в атмосферный воздух, вторичных загрязнителей, более опасных, чем исходные.', 
            self
        )
        self.info_beta_label.setGeometry(50, 320, 700, 60)
        self.info_beta_label.setWordWrap(True)
        self.beta_label = QLabel("Выберите поправку (β)", self)
        self.beta_label.setGeometry(50, 365, 300, 30)
        self.beta_combo = QComboBox(self)
        self.beta_combo.setGeometry(225, 370, 400, 30)
        self.beta_combo.addItems(["5", "2", "1"])

        self.explain_beta_button = QPushButton("?", self)
        self.explain_beta_button.setFixedSize(50, 50)
        self.explain_beta_button.clicked.connect(self.show_explain_beta_value)
        self.explain_beta_button.move(650, 360)

        self.image_instruction_label = QLabel(
            "Загрузите топооснову в формате PNG, JPG, JPEG или BMP с размерами (1×1, 5×5 или 10×10 км.)",
            self
        )
        self.image_instruction_label.setGeometry(150, 460, 500, 40)
        self.image_instruction_label.setWordWrap(True)
        self.image_button = QPushButton("Выбрать топооснову", self)
        self.image_button.setGeometry(300, 500, 200, 50)
        self.image_button.clicked.connect(self.select_image)

        self.save_button = QPushButton("Расчитать", self)
        self.save_button.setGeometry(300, 630, 200, 50)
        self.save_button.clicked.connect(self.save_values)

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите топооснову", "", 
                                                  "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", 
                                                  options=options)
        if file_name:
            self.selected_image_path = file_name
            self.image_button.setStyleSheet("")  # Сбрасываем стиль, если был красный
        else:
            self.selected_image_path = None

    def show_explain_c_value(self):
        explanation = (
            "Значения поправки c принимаются:\n\n"
            "c = 5 - для токсичных материалов и их оксидов – ванадия, марганца, кобальта, никеля, хрома, "
            "цинка, мышьяка, серебра, кадмия, сурьмы, олова, платины, ртути, свинца, урана;\n\n"
            "c = 2 - для прочих металлов и их оксидов – натрия, магния, калия, кальция, железа, стронция, "
            "молибдена, бария, вольфрама, висмута, кремния, бериллия, а также для других компонентов твердых "
            "аэрозолей, полициклических ароматических углеводородов, в том числе 3,4 – бенз(а)пирена;\n\n"
            "c = 1 - для всех прочих выбрасываемых в атмосферный воздух загрязнителей (газов, кислот и щелочей в "
            "аэрозолях и др.)"
        )
        explanation_dialog = ExplanationDialog(explanation)
        explanation_dialog.exec_()

    def show_explain_delta_value(self):
        delta_i_explanation = (
            "Значения поправки δ принимаются:\n\n"
            "δ = 2 - для выбрасываемых и испаряющихся в атмосферный воздух легко диссоциирующих кислот и щелочей "
            "(фтористого водорода, соляной и серной кислот и др.);\n\n"
            "δ = 1,5 - для сернистого газа, оксидов азота, сероводорода, сероуглерода, озона, хорошо растворимых "
            "неорганических соединений фтора;\n\n"
            "δ = 1,2 - для органической пыли, содержащей ПАУ и другие опасные соединения, для токсичных металлов "
            "и их оксидов, реактивной органики (альдегидов и т.п.), аммиака, неорганических соединений кремния, "
            "плохо растворимых соединений фтора, оксида углерода, легких углеводородов;\n\n"
            "δ = 1 - для прочих соединений и примесей (органических пылей, нетоксичных металлов и их оксидов, "
            "в том числе натрия, магния, калия, кальция, железа, стронция, молибдена, бария, вольфрама, висмута и др.)"
        )
        delta_i_dialog = ExplanationDialog(delta_i_explanation)
        delta_i_dialog.exec_()

    def show_explain_lambda_value(self):
        lambda_i_explanation = (
            "Значения поправки λ принимаются:\n\n"
            "λ = 1,2 - для твердых аэрозолей (пылей), выбрасываемых на территориях со среднегодовым количеством осадков "
            "менее 400 мм в год;\n\n"
            "λ = 1 - для всех остальных случаев."
        )
        lambda_i_dialog = ExplanationDialog(lambda_i_explanation)
        lambda_i_dialog.exec_()

    def show_explain_beta_value(self):
        beta_i_explanation = (
            "Значения поправки β принимаются:\n\n"
            "β = 5 - для нетоксичных летучих углеводородов при поступлении их в атмосферный воздух южнее 40 град. Северной широты;\n\n"
            "β = 2 - для тех же веществ при поступлении их в атмосферный воздух севернее 40 град. Северной широты;\n\n"
            "β = 1 - для прочих веществ."
        )
        beta_i_dialog = ExplanationDialog(beta_i_explanation)
        beta_i_dialog.exec_()

    def save_values(self):
        if not self.selected_image_path:
            # Показываем сообщение об ошибке
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите изображение перед продолжением.")
            # Подсвечиваем кнопку красным
            self.image_button.setStyleSheet("background-color: #ff9999;")
            return
            
        c_value = self.c_combo.currentText()
        delta_value = self.delta_combo.currentText()
        lambda_value = self.lambda_combo.currentText()
        beta_value = self.beta_combo.currentText()
        self.data['c'] = c_value
        self.data['delta'] = delta_value
        self.data['lambda'] = lambda_value
        self.data['beta'] = beta_value
        self.data['image_path'] = self.selected_image_path

        self.new_window = ResultHomogeneousWindow(self.data)
        self.new_window.show()
        self.close()


class ResultHomogeneousWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.source_point = None
        self.inner_radius_m = 0
        self.outer_radius_m = 0
        self.economic_damage = 0
        self.original_pixmap = None
        self.current_scale = 1.0
        self.physical_rect = None
        self.setting_source = False
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Результаты расчета загрязнения")
        self.setGeometry(100, 100, 1100, 800)

        # Main layout
        layout = QVBoxLayout()

        # Header with scale selection
        header = QWidget()
        header_layout = QHBoxLayout(header)
        
        scale_label = QLabel("Масштаб карты:")
        self.scale_combo = QComboBox()
        self.scale_combo.addItems(["1x1 км", "5x5 км", "10x10 км"])
        self.scale_combo.currentIndexChanged.connect(self.change_scale)
        
        header_layout.addWidget(QLabel(f"Загрязняющее вещество: {self.data['pollutant_name']}"))
        header_layout.addStretch()
        header_layout.addWidget(scale_label)
        header_layout.addWidget(self.scale_combo)
        
        layout.addWidget(header)

        # Content area
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)

        # Image area (70%)
        image_widget = QWidget()
        image_layout = QVBoxLayout(image_widget)
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(700, 700)
        self.image_label.setStyleSheet("border: 2px solid #ccc; background: #f8f8f8;")
        self.image_label.mousePressEvent = self.handle_image_click
        image_layout.addWidget(self.image_label)

        # Image controls
        controls_widget = QWidget()
        controls_layout = QHBoxLayout(controls_widget)
        
        self.btn_set_source = QPushButton("Установить стационарный источник выбросов")
        self.btn_set_source.clicked.connect(self.enable_source_selection)
        
        self.btn_reset = QPushButton("Сбросить")
        self.btn_reset.clicked.connect(self.reset_source_point)
        
        controls_layout.addStretch()
        controls_layout.addWidget(self.btn_set_source)
        controls_layout.addWidget(self.btn_reset)
        controls_layout.addStretch()
        
        image_layout.addWidget(controls_widget)

        # Info panel (30%)
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        
        info_title = QLabel("Результаты расчета")
        info_title.setStyleSheet("font-weight: bold; font-size: 16px; margin-bottom: 15px;")
        
        self.results_label = QLabel()
        self.results_label.setStyleSheet("""
            font-size: 14px; 
            padding: 10px;
            line-height: 1.5;
        """)
        
        info_layout.addWidget(info_title)
        info_layout.addWidget(self.results_label)
        info_layout.addStretch()

        # Add to content layout
        content_layout.addWidget(image_widget, 70)
        content_layout.addWidget(info_widget, 30)

        # Add to main layout
        layout.addWidget(content_widget)
        self.setLayout(layout)

        # Initial setup
        self.change_scale()
        self.calculate_pollution()
        self.display_image(self.data['image_path'])

    def enable_source_selection(self):
        self.setting_source = True
        self.image_label.setCursor(Qt.CrossCursor)
        QMessageBox.information(self, "Местоположение источника выбросов", 
                              "Нажмите на топооснову, чтобы установить местоположение источника выбросов")

    def change_scale(self):
        scale_text = self.scale_combo.currentText()
        if scale_text == "1x1 км":
            self.current_scale = 1.0
        elif scale_text == "5x5 км":
            self.current_scale = 5.0
        elif scale_text == "10x10 км":
            self.current_scale = 10.0
            
        self.physical_rect = QRectF(0, 0, 1000 * self.current_scale, 1000 * self.current_scale)
        
        if self.original_pixmap:
            self.update_image()
        self.calculate_pollution()

    def calculate_pollution(self):
        thermal_correction = 1 + ((float(self.data['temperature_mixture']) - 
                                 float(self.data['average_temperature'])) / 75)  
        self.inner_radius_m = 2 * thermal_correction * float(self.data['height_of_emission'])
        self.outer_radius_m = 20 * thermal_correction * float(self.data['height_of_emission'])     
        koef_a = pow((60 / (float(self.data['average_PDK']) * float(self.data['max_PDK']))), 0.5)
        ai = koef_a * float(self.data['c']) * float(self.data['delta']) * float(self.data['lambda']) * float(self.data['beta'])
        gross_emission = ai * float(self.data['ejection_mass'])
        popravka_f = pow((100 / (100 + thermal_correction * float(self.data['height_of_emission']))), 2) * (4 / (1 + float(self.data['average_wind'])))
        self.economic_damage = (float(self.data['const_to_rubles']) * 
                              float(self.data['hazard_index']) * 
                              gross_emission * 
                              float(self.data['deflator']) * 
                              popravka_f)
        self.update_results_label()

    def update_results_label(self):
        # Рассчитываем площадь зоны загрязнения
        area = math.pi * (self.outer_radius_m**2 - self.inner_radius_m**2)
        
        # Форматируем числа с разделителями тысяч
        formatted_inner = "{:,.1f}".format(self.inner_radius_m).replace(",", " ")
        formatted_outer = "{:,.1f}".format(self.outer_radius_m).replace(",", " ")
        formatted_area = "{:,.1f}".format(area).replace(",", " ")
        formatted_damage = "{:,.2f}".format(self.economic_damage).replace(",", " ")
        
        results_text = f"""
        <b>Тип загрязняемой местности:</b> {self.data['terrain_type']}<br><br>
        
        <b>Характеристика зоны активного загрязнения:</b><br>
        - Внутренний радиус: {formatted_inner} м<br>
        - Внешний радиус: {formatted_outer} м<br>
        - Площадь зоны: {formatted_area} м²<br><br>
        
        <b>Экономический ущерб атмосферному воздуху:</b><br>
        {formatted_damage} руб./усл. т
        """
        
        self.results_label.setText(results_text)

    def handle_image_click(self, event):
        if not self.setting_source or not self.original_pixmap:
            return

        click_pos = event.pos()
        displayed_pix = self.image_label.pixmap()
        if not displayed_pix:
            return

        img_width = displayed_pix.width()
        img_height = displayed_pix.height()
        label_width = self.image_label.width()
        label_height = self.image_label.height()
        
        x_offset = (label_width - img_width) / 2
        y_offset = (label_height - img_height) / 2
        
        img_x = click_pos.x() - x_offset
        img_y = click_pos.y() - y_offset
        
        if 0 <= img_x < img_width and 0 <= img_y < img_height:
            original_x = img_x * (self.original_pixmap.width() / img_width)
            original_y = img_y * (self.original_pixmap.height() / img_height)
            
            self.source_point = QPointF(original_x, original_y)
            self.btn_set_source.setEnabled(False)
            self.setting_source = False
            self.image_label.setCursor(Qt.ArrowCursor)
            self.update_image()

    def reset_source_point(self):
        self.source_point = None
        self.btn_set_source.setEnabled(True)
        self.update_image()

    def display_image(self, file_path):
        self.original_pixmap = QPixmap(file_path)
        if self.original_pixmap.isNull():
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение карты")
            return
            
        self.update_image()

    def update_image(self):
        if not self.original_pixmap:
            return

        temp_pixmap = QPixmap(self.original_pixmap.size())
        temp_pixmap.fill(Qt.transparent)
        
        painter = QPainter(temp_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPixmap(0, 0, self.original_pixmap)
        
        if self.source_point:
            meters_to_pixels = self.original_pixmap.width() / (1000 * self.current_scale)
            
            inner_px = self.inner_radius_m * meters_to_pixels
            outer_px = self.outer_radius_m * meters_to_pixels
            
            painter.setPen(QPen(QColor(255,0,0,80), 2))
            painter.setBrush(QBrush(QColor(255,0,0,30)))
            painter.drawEllipse(self.source_point, outer_px, outer_px)
            
            painter.setPen(QPen(QColor(255,165,0,120), 2))
            painter.setBrush(QBrush(QColor(255,165,0,60)))
            painter.drawEllipse(self.source_point, inner_px, inner_px)
            
            painter.setPen(QPen(Qt.black, 3))
            painter.setBrush(QBrush(Qt.red))
            painter.drawEllipse(self.source_point, 5, 5)
        
        painter.end()
        
        scaled_pixmap = temp_pixmap.scaled(
            self.image_label.width(),
            self.image_label.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)


class FirstHeterogeneousWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Неоднородный тип местности")
        self.setGeometry(100, 100, 800, 720)

        # Левая колонка (поля ввода)
        self.name_pollutant_input = QLineEdit(self)
        self.name_pollutant_input.setGeometry(50, 50, 300, 30)
        
        self.average_PDK_input = QLineEdit(self)
        self.average_PDK_input.setGeometry(50, 100, 300, 30)
        
        self.max_PLD_input = QLineEdit(self)
        self.max_PLD_input.setGeometry(50, 150, 300, 30)
        
        self.ejection_mass_input = QLineEdit(self)
        self.ejection_mass_input.setGeometry(50, 200, 300, 30)
        
        self.height_of_emission_input = QLineEdit(self)
        self.height_of_emission_input.setGeometry(50, 250, 300, 30)
        
        self.emission_clean_factor_input = QLineEdit(self)
        self.emission_clean_factor_input.setGeometry(50, 300, 300, 30)
        
        self.temperature_mixture_input = QLineEdit(self)
        self.temperature_mixture_input.setGeometry(50, 350, 300, 30)
        
        self.average_temperature_input = QLineEdit(self)
        self.average_temperature_input.setGeometry(50, 400, 300, 30)
        
        self.average_wind_input = QLineEdit(self)
        self.average_wind_input.setGeometry(50, 450, 300, 30)
        
        self.const_to_rubles_input = QLineEdit(self)
        self.const_to_rubles_input.setGeometry(50, 500, 300, 30)
        
        self.deflator_input = QLineEdit(self)
        self.deflator_input.setGeometry(50, 550, 300, 30)

        # Правая колонка (подписи)
        self.name_label = QLabel("Наименование загрязняющего вещества", self)
        self.name_label.setGeometry(375, 50, 400, 30)
        self.name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.average_PDK_label = QLabel("ПДК среднесуточная, мг/м3", self)
        self.average_PDK_label.setGeometry(375, 100, 400, 30)
        self.average_PDK_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.max_PDK_label = QLabel("ПДК максимально-разовая, мг/м3", self)
        self.max_PDK_label.setGeometry(375, 150, 400, 30)
        self.max_PDK_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.ejection_mass_label = QLabel("Масса валового выброса (m), т/год", self)
        self.ejection_mass_label.setGeometry(375, 200, 400, 30)
        self.ejection_mass_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.height_of_emission_label = QLabel("Высота стационарного источника выбросов (H), м", self)
        self.height_of_emission_label.setGeometry(375, 250, 400, 30)
        self.height_of_emission_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.emission_clean_factor_label = QLabel("Эффективность очистки выбросов, %", self)
        self.emission_clean_factor_label.setGeometry(375, 300, 400, 30)
        self.emission_clean_factor_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.temperature_mixture_label = QLabel("Температура выброса, Сº", self)
        self.temperature_mixture_label.setGeometry(375, 350, 400, 30)
        self.temperature_mixture_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.average_temperature_label = QLabel("Среднегодовая температура атмосферного воздуха, Сº", self)
        self.average_temperature_label.setGeometry(375, 400, 400, 30)
        self.average_temperature_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.average_wind_label = QLabel("Среднегодовая сила ветра (U), м/с", self)
        self.average_wind_label.setGeometry(375, 450, 400, 30)
        self.average_wind_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
 
        self.const_to_rubles_label = QLabel("Удельный экономический ущерб от выбросов\nусловной тонны загрязняющего вещества, руб. усл/т", self)
        self.const_to_rubles_label.setGeometry(375, 500, 400, 30)
        self.const_to_rubles_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.deflator_label = QLabel("Коэффициент-дефлятор", self)
        self.deflator_label.setGeometry(375, 550, 400, 30)
        self.deflator_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Кнопки
        self.save_button = QPushButton("Сохранить", self)
        self.save_button.setFixedSize(200, 50)
        self.save_button.clicked.connect(self.validate_and_save)
        self.save_button.move(510, 650)

        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(200, 50)
        self.back_button.clicked.connect(self.close_first_heterogeneous_window)
        self.back_button.move(50, 650)

    def validate_and_save(self):
        """Проверяем данные перед сохранением"""
        fields = [
            ('pollutant_name', self.name_pollutant_input, False),
            ('average_PDK', self.average_PDK_input, True),
            ('max_PDK', self.max_PLD_input, True),
            ('ejection_mass', self.ejection_mass_input, True),
            ('height_of_emission', self.height_of_emission_input, True),
            ('emission_clean_factor', self.emission_clean_factor_input, True),
            ('temperature_mixture', self.temperature_mixture_input, True),
            ('average_temperature', self.average_temperature_input, True),
            ('average_wind', self.average_wind_input, True),
            ('const_to_rubles', self.const_to_rubles_input, True),
            ('deflator', self.deflator_input, True)
        ]
        
        data = {}
        errors = []
        
        for name, field, is_numeric in fields:
            value = field.text().strip()
            
            if not value:
                errors.append(f"Поле '{name}' не заполнено")
                continue
                
            if is_numeric:
                # Заменяем запятые на точки для корректного преобразования
                value = value.replace(',', '.')
                try:
                    float(value)
                except ValueError:
                    errors.append(f"Поле '{name}' должно содержать число")
                    continue
                    
            data[name] = value
        
        if errors:
            QMessageBox.warning(
                self, 
                "Ошибки ввода", 
                "Обнаружены следующие ошибки:\n\n• " + "\n• ".join(errors)
            )
            return
            
        self.save_data(data)

    def save_data(self, data):
        """Сохранение данных и переход к следующему окну"""
        # Преобразуем числовые значения
        numeric_fields = [
            'average_PDK', 'max_PDK', 'ejection_mass', 
            'height_of_emission', 'emission_clean_factor',
            'temperature_mixture', 'average_temperature',
            'average_wind', 'const_to_rubles', 'deflator',
            'hazard_index'
        ]
        
        processed_data = {}
        for key, value in data.items():
            if key in numeric_fields:
                processed_data[key] = float(value.replace(',', '.'))
            else:
                processed_data[key] = value
        
        self.new_window = SecondHeterogeneousWindow(processed_data)
        self.new_window.show()
        self.close()

    def close_first_heterogeneous_window(self):
        self.close()
        self.main_window.show()


class SecondHeterogeneousWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.selected_image_path = None  # Добавляем атрибут для хранения пути к изображению
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Неоднородный тип местности")
        self.setGeometry(100, 100, 800, 720)

        # C 
        self.info_c_label = QLabel(
            "c – поправка, учитывающая вероятность накопления исходной примеси или вторичных загрязнителей в компонентах окружающей среды и цепях питания, "
            "а также поступления примеси в организм человека неингаляционным путем.",
            self
        )
        self.info_c_label.setGeometry(50, 20, 700, 60)
        self.info_c_label.setWordWrap(True)
        self.c_label = QLabel("Выберите поправку (c):", self)
        self.c_label.setGeometry(50, 90, 300, 30)
        self.c_combo = QComboBox(self)
        self.c_combo.setGeometry(225, 90, 400, 30)
        self.c_combo.addItems(["5", "2", "1"])

        self.explain_c_button = QPushButton("?", self)
        self.explain_c_button.setFixedSize(50, 50)
        self.explain_c_button.clicked.connect(self.show_explain_c_value)
        self.explain_c_button.move(650, 75)

        # delta
        self.info_delta_label = QLabel(
            "δ – поправка, характеризующая вредное воздействие примеси на реципиентов (за исключением человека)",
            self
        )
        self.info_delta_label.setGeometry(50, 120, 700, 60)
        self.info_delta_label.setWordWrap(True)
        self.delta_label = QLabel("Выберите поправку (δ)", self)
        self.delta_label.setGeometry(50, 180, 300, 30)
        self.delta_combo = QComboBox(self)
        self.delta_combo.setGeometry(225, 180, 400, 30)
        self.delta_combo.addItems(["2", "1.5", "1.2", "1"])

        self.explain_delta_button = QPushButton("?", self)
        self.explain_delta_button.setFixedSize(50, 50)
        self.explain_delta_button.clicked.connect(self.show_explain_delta_value)
        self.explain_delta_button.move(650, 170)

        # Lambda
        self.info_lambda_label = QLabel(
            'λ – поправка на вероятность вторичного заброса примесей в атмосферный воздух после их оседания на поверхностях.',
            self
        )
        self.info_lambda_label.setGeometry(50, 220, 700, 60)
        self.info_lambda_label.setWordWrap(True)
        self.lambda_label = QLabel("Выберите поправку (λ)", self)
        self.lambda_label.setGeometry(50, 270, 300, 30)
        self.lambda_combo = QComboBox(self)
        self.lambda_combo.setGeometry(225, 270, 400, 30)
        self.lambda_combo.addItems(["1.2", "1"])

        self.explain_lambda_button = QPushButton("?", self)
        self.explain_lambda_button.setFixedSize(50, 50)
        self.explain_lambda_button.clicked.connect(self.show_explain_lambda_value)
        self.explain_lambda_button.move(650, 265)

        self.info_beta_label = QLabel(
            'β – поправка на вероятность образования из исходных примесей, выброшенных в атмосферный воздух, вторичных загрязнителей, более опасных, чем исходные.', 
            self
        )
        self.info_beta_label.setGeometry(50, 320, 700, 60)
        self.info_beta_label.setWordWrap(True)
        self.beta_label = QLabel("Выберите поправку (β)", self)
        self.beta_label.setGeometry(50, 365, 300, 30)
        self.beta_combo = QComboBox(self)
        self.beta_combo.setGeometry(225, 370, 400, 30)
        self.beta_combo.addItems(["5", "2", "1"])

        self.explain_beta_button = QPushButton("?", self)
        self.explain_beta_button.setFixedSize(50, 50)
        self.explain_beta_button.clicked.connect(self.show_explain_beta_value)
        self.explain_beta_button.move(650, 360)

        self.image_instruction_label = QLabel(
            "Загрузите топооснову в формате PNG, JPG, JPEG или BMP с размерами (1×1, 5×5 или 10×10 км.)",
            self
        )
        self.image_instruction_label.setGeometry(150, 460, 500, 40)
        self.image_instruction_label.setWordWrap(True)
        self.image_button = QPushButton("Выбрать топооснову", self)
        self.image_button.setGeometry(300, 500, 200, 50)
        self.image_button.clicked.connect(self.select_image)

        self.save_button = QPushButton("Расчитать", self)
        self.save_button.setGeometry(300, 630, 200, 50)
        self.save_button.clicked.connect(self.save_values)

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", 
                                                  "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", 
                                                  options=options)
        if file_name:
            self.selected_image_path = file_name
            self.image_button.setStyleSheet("")  # Сбрасываем стиль, если был красный
        else:
            self.selected_image_path = None

    def show_explain_c_value(self):
        explanation = (
            "Значения поправки c принимаются:\n\n"
            "c = 5 - для токсичных материалов и их оксидов – ванадия, марганца, кобальта, никеля, хрома, "
            "цинка, мышьяка, серебра, кадмия, сурьмы, олова, платины, ртути, свинца, урана;\n\n"
            "c = 2 - для прочих металлов и их оксидов – натрия, магния, калия, кальция, железа, стронция, "
            "молибдена, бария, вольфрама, висмута, кремния, бериллия, а также для других компонентов твердых "
            "аэрозолей, полициклических ароматических углеводородов, в том числе 3,4 – бенз(а)пирена;\n\n"
            "c = 1 - для всех прочих выбрасываемых в атмосферный воздух загрязнителей (газов, кислот и щелочей в "
            "аэрозолях и др.)"
        )
        explanation_dialog = ExplanationDialog(explanation)
        explanation_dialog.exec_()

    def show_explain_delta_value(self):
        delta_i_explanation = (
            "Значения поправки δ принимаются:\n\n"
            "δ = 2 - для выбрасываемых и испаряющихся в атмосферный воздух легко диссоциирующих кислот и щелочей "
            "(фтористого водорода, соляной и серной кислот и др.);\n\n"
            "δ = 1,5 - для сернистого газа, оксидов азота, сероводорода, сероуглерода, озона, хорошо растворимых "
            "неорганических соединений фтора;\n\n"
            "δ = 1,2 - для органической пыли, содержащей ПАУ и другие опасные соединения, для токсичных металлов "
            "и их оксидов, реактивной органики (альдегидов и т.п.), аммиака, неорганических соединений кремния, "
            "плохо растворимых соединений фтора, оксида углерода, легких углеводородов;\n\n"
            "δ = 1 - для прочих соединений и примесей (органических пылей, нетоксичных металлов и их оксидов, "
            "в том числе натрия, магния, калия, кальция, железа, стронция, молибдена, бария, вольфрама, висмута и др.)"
        )
        delta_i_dialog = ExplanationDialog(delta_i_explanation)
        delta_i_dialog.exec_()

    def show_explain_lambda_value(self):
        lambda_i_explanation = (
            "Значения поправки λ принимаются:\n\n"
            "λ = 1,2 - для твердых аэрозолей (пылей), выбрасываемых на территориях со среднегодовым количеством осадков "
            "менее 400 мм в год;\n\n"
            "λ = 1 - для всех остальных случаев."
        )
        lambda_i_dialog = ExplanationDialog(lambda_i_explanation)
        lambda_i_dialog.exec_()

    def show_explain_beta_value(self):
        beta_i_explanation = (
            "Значения поправки β принимаются:\n\n"
            "β = 5 - для нетоксичных летучих углеводородов при поступлении их в атмосферный воздух южнее 40 град. Северной широты;\n\n"
            "β = 2 - для тех же веществ при поступлении их в атмосферный воздух севернее 40 град. Северной широты;\n\n"
            "β = 1 - для прочих веществ."
        )
        beta_i_dialog = ExplanationDialog(beta_i_explanation)
        beta_i_dialog.exec_()

    def save_values(self):
        if not self.selected_image_path:
            # Показываем сообщение об ошибке
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите изображение перед продолжением.")
            # Подсвечиваем кнопку красным
            self.image_button.setStyleSheet("background-color: #ff9999;")
            return
            
        c_value = self.c_combo.currentText()
        delta_value = self.delta_combo.currentText()
        lambda_value = self.lambda_combo.currentText()
        beta_value = self.beta_combo.currentText()
        self.data['c'] = c_value
        self.data['delta'] = delta_value
        self.data['lambda'] = lambda_value
        self.data['beta'] = beta_value
        self.data['image_path'] = self.selected_image_path

        self.new_window = ResultHeterogeneousWindow(self.data)
        self.new_window.show()
        self.close()


class ExplanationDialog(QDialog):
    def __init__(self, explanation_text):
        super().__init__()
        self.setWindowTitle("Пояснение")
        self.setGeometry(200, 200, 600, 400)
        
        layout = QVBoxLayout()
        
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(explanation_text)
        self.text_edit.setReadOnly(True)
        
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.close)
        
        layout.addWidget(self.text_edit)
        layout.addWidget(ok_button)
        
        self.setLayout(layout)


class ResultHeterogeneousWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.source_point = None
        self.inner_radius_m = 0
        self.outer_radius_m = 0
        self.selected_zones = []
        self.current_zone_points = []
        self.is_selecting_zone = False
        self.setting_source = False
        self.original_pixmap = None
        self.current_scale = 1.0
        self.physical_rect = None
        
        # Словарь типов местности и их коэффициентов
        self.terrain_types = {
            "Территории курортов, заповедников, заказников": 10,
            "Территории природных зон отдыха и садовых участков, парков": 8,
            "Территория населенных пунктов с плотностью населения n чел/га": 10,
            "Территория населенных пунктов с плотностью более 300 чел./га": 8,
            "Территории промышленных предприятий (включая санитарно-защитную зону)": 4,
            "Леса: 1-я группа": 0.2,
            "Леса: 2-я группа": 0.1,
            "Леса: 3-я группа": 0.025,
            "Пашни: Южные зоны (южнее 50 гр. Северной широты)": 0.25,
            "Пашни: Центральный черноземный район, южная Сибирь": 0.15,
            "Пашни: Прочие районы": 0.1,
            "Сады, виноградники": 0.5,
            "Пастбища, сенокосы": 0.05
        }
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Неоднородный тип местности")
        self.setGeometry(100, 100, 1400, 850)  # Увеличиваем ширину окна

        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)

        # Header (без изменений)
        header = QWidget()
        header_layout = QHBoxLayout(header)
        scale_label = QLabel("Масштаб карты:")
        self.scale_combo = QComboBox()
        self.scale_combo.addItems(["1x1 км", "5x5 км", "10x10 км"])
        self.scale_combo.currentIndexChanged.connect(self.change_scale)
        
        header_layout.addWidget(QLabel(f"Загрязняющее вещество: {self.data['pollutant_name']}"))
        header_layout.addStretch()
        header_layout.addWidget(scale_label)
        header_layout.addWidget(self.scale_combo)
        layout.addWidget(header)

        # Content area
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(10)

        # Image area (фиксированный размер карты)
        image_container = QWidget()
        image_layout = QVBoxLayout(image_container)
        image_layout.setContentsMargins(0, 0, 0, 0)
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(800, 600)  # Фиксированный размер карты
        self.image_label.setStyleSheet("border: 2px solid #ccc; background: #f8f8f8;")
        self.image_label.mousePressEvent = self.handle_image_click
        image_layout.addWidget(self.image_label, 0, Qt.AlignCenter)  # Центрируем карту

        # Controls (без изменений)
        controls_widget = QWidget()
        controls_layout = QHBoxLayout(controls_widget)
        self.btn_set_source = QPushButton("Установить стационарный источник выбросов")
        self.btn_set_source.clicked.connect(self.enable_source_selection)
        self.btn_add_zone = QPushButton("Добавить тип загрязняемой местности\nи указать на топооснове его площадь")
        self.btn_add_zone.setEnabled(False)
        self.btn_add_zone.clicked.connect(self.start_zone_selection)
        self.btn_finish_zone = QPushButton("Сохранить")
        self.btn_finish_zone.setEnabled(False)
        self.btn_finish_zone.clicked.connect(self.finish_zone_selection)
        self.btn_reset = QPushButton("Сбросить")
        self.btn_reset.clicked.connect(self.reset_zones)
        
        controls_layout.addStretch()
        controls_layout.addWidget(self.btn_set_source)
        controls_layout.addWidget(self.btn_add_zone)
        controls_layout.addWidget(self.btn_finish_zone)
        controls_layout.addWidget(self.btn_reset)
        controls_layout.addStretch()
        
        image_layout.addWidget(controls_widget)

        # Zones panel - расширенная версия
        zones_container = QWidget()
        zones_layout = QVBoxLayout(zones_container)
        zones_layout.setContentsMargins(0, 0, 0, 0)
        
        # Заголовки
        self.pollution_area_label = QLabel("Площадь зоны активного загрязнения: 0 м²")
        self.pollution_area_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        zones_layout.addWidget(self.pollution_area_label)
        
        zones_title = QLabel("Характеристика загрязняемой местности")
        zones_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        zones_layout.addWidget(zones_title)

        # Таблица - теперь шире
        self.zones_table = QTableWidget()
        self.zones_table.setColumnCount(4)
        self.zones_table.setHorizontalHeaderLabels([
            "Тип местности", 
            "Площадь (м²)", 
            "Показатель относительной опасности", 
            "Доля вклада, %"
        ])
        
        # Настройки колонок
        self.zones_table.setColumnWidth(0, 350)  # Широкая первая колонка
        self.zones_table.setColumnWidth(1, 150)
        self.zones_table.setColumnWidth(2, 200)
        self.zones_table.setColumnWidth(3, 150)
        self.zones_table.horizontalHeader().setStretchLastSection(True)
        
        # Кнопка расчета
        self.btn_calculate = QPushButton("Рассчитать экономический ущерб")
        self.btn_calculate.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 8px;")
        self.btn_calculate.clicked.connect(self.calculate_damage)
        
        zones_layout.addWidget(self.zones_table, 1)
        zones_layout.addWidget(self.btn_calculate)

        # Компоновка
        content_layout.addWidget(image_container)
        content_layout.addWidget(zones_container, 1)  # Растягиваем только правую панель
        
        layout.addWidget(content_widget, 1)
        self.setLayout(layout)

        # Инициализация
        self.change_scale()
        self.calculate_pollution()
        self.display_image(self.data['image_path'])

    def change_scale(self):
        """Change map scale and recalculate all parameters"""
        scale_text = self.scale_combo.currentText()
        if scale_text == "1x1 км":
            self.current_scale = 1.0
        elif scale_text == "5x5 км":
            self.current_scale = 5.0
        elif scale_text == "10x10 км":
            self.current_scale = 10.0
            
        self.physical_rect = QRectF(0, 0, 1000 * self.current_scale, 1000 * self.current_scale)
        
        if self.original_pixmap:
            self.update_image()
        self.calculate_pollution()
        self.update_zones_table()

    def calculate_pollution(self):
        """Calculate pollution parameters for current scale"""
        thermal_correction = 1 + ((float(self.data['temperature_mixture']) - 
                                 float(self.data['average_temperature'])) / 75)
        
        # Радиусы в метрах (не зависят от масштаба карты)
        self.inner_radius_m = 2 * thermal_correction * float(self.data['height_of_emission'])
        self.outer_radius_m = 20 * thermal_correction * float(self.data['height_of_emission'])
        
        # Расчет агрессивности выбросов
        koef_a = sqrt(60 / (float(self.data['average_PDK']) * float(self.data['max_PDK'])))
        self.aggressive_indicator = koef_a * float(self.data['c']) * float(self.data['delta']) * float(self.data['lambda']) * float(self.data['beta'])
        self.gross_emission_mass = self.aggressive_indicator * float(self.data['ejection_mass'])
        self.popravka_f = (100 / (100 + thermal_correction * float(self.data['height_of_emission'])))**2 * (4 / (1 + float(self.data['average_wind'])))

        # Обновляем площадь загрязнения
        pollution_area = pi * (self.outer_radius_m**2 - self.inner_radius_m**2)
        self.pollution_area_label.setText(f"Площадь зоны активного загрязнения: {pollution_area:.0f} м²")

    def enable_source_selection(self):
        """Enable source point selection mode"""
        self.setting_source = True
        self.image_label.setCursor(Qt.CrossCursor)
        QMessageBox.information(self, "Местоположение источника выбросов", 
                              "Нажмите на карту, чтобы установить местоположение источника выбросов")

    def start_zone_selection(self):
        """Begin zone creation mode with terrain type selection"""
        if not self.source_point:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, сначала установите исходную точку!")
            return
            
        # Показываем диалог выбора типа местности
        dialog = QDialog(self)
        dialog.setWindowTitle("Выбор типа местности")
        dialog.setFixedSize(800, 600)
        
        scroll = QScrollArea(dialog)
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        
        group_box = QGroupBox("Выберите тип местности:", dialog)
        group_layout = QVBoxLayout()
        
        self.terrain_button_group = QButtonGroup(dialog)
        
        for i, (terrain, value) in enumerate(self.terrain_types.items()):
            radio = QRadioButton(f"{terrain} (коэффициент опасности: {value})", dialog)
            radio.setStyleSheet("font-size: 12px; padding: 5px;")
            self.terrain_button_group.addButton(radio, i)
            group_layout.addWidget(radio)
        
        group_box.setLayout(group_layout)
        layout.addWidget(group_box)
        
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        
        confirm_button = QPushButton("Подтвердить", dialog)
        confirm_button.setFixedSize(200, 40)
        confirm_button.clicked.connect(lambda: self.start_zone_after_selection(dialog))
        
        cancel_button = QPushButton("Отмена", dialog)
        cancel_button.setFixedSize(200, 40)
        cancel_button.clicked.connect(dialog.close)
        
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(cancel_button)
        layout.addWidget(button_container)
        
        scroll.setWidget(content)
        dialog_layout = QVBoxLayout(dialog)
        dialog_layout.addWidget(scroll)
        
        dialog.exec_()


    def start_zone_after_selection(self, dialog):
        """Start zone selection after terrain type is chosen"""
        selected_button = self.terrain_button_group.checkedButton()
        if not selected_button:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите тип местности")
            return
            
        # Получаем выбранный тип местности и коэффициент
        terrain_text = selected_button.text().split(" (коэффициент опасности: ")[0]
        hazard_value = self.terrain_types[terrain_text]
        
        # Запоминаем текущий тип местности для новой зоны
        self.current_terrain_type = terrain_text
        self.current_hazard_value = hazard_value
        
        # Начинаем создание зоны
        self.is_selecting_zone = True
        self.current_zone_points = []
        self.image_label.setCursor(Qt.CrossCursor)
        self.btn_finish_zone.setEnabled(False)
        dialog.close()
        
        QMessageBox.information(self, "Добавление типа загрязняемой местности", 
                              f"Выбран тип: {terrain_text}\n"
                              f"Коэффициент опасности: {hazard_value}\n\n"
                              "Нажмите на топооснову и отметьте не менее 3 точек, чтобы выделить участок выбранного типа местности - убедитесь, что указанный участок попадает в зону активного загрязнения, после чего нажмите 'Сохранить' для завершения действия "
                            )


    def finish_zone_selection(self):
        """Complete the current zone and add to list"""
        if len(self.current_zone_points) < 3:
            QMessageBox.warning(self, "Ошибка", "Зона должна иметь минимум 3 точки!")
            return

        polygon = QPolygon(self.current_zone_points)
        zone_area = self.calculate_polygon_area(polygon)  # Area in pixels
        
        # Convert to meters (considering current scale)
        meters_to_pixels = self.original_pixmap.width() / (1000 * self.current_scale)
        actual_area = zone_area / (meters_to_pixels ** 2)  # Area in m²
        
        # Добавляем зону с информацией о типе местности
        self.selected_zones.append({
            'polygon': polygon,
            'area': actual_area,
            'terrain_type': self.current_terrain_type,
            'coefficient': self.current_hazard_value,
            'contribution': 0.0   # Will be calculated
        })
        
        self.update_zones_table()
        self.current_zone_points = []
        self.is_selecting_zone = False
        self.image_label.setCursor(Qt.ArrowCursor)
        self.btn_finish_zone.setEnabled(False)
        self.update_image()

    def reset_zones(self):
        """Reset all zones and source point"""
        self.source_point = None
        self.selected_zones = []
        self.current_zone_points = []
        self.is_selecting_zone = False
        self.setting_source = False
        self.btn_set_source.setEnabled(True)
        self.btn_add_zone.setEnabled(False)
        self.btn_finish_zone.setEnabled(False)
        self.image_label.setCursor(Qt.ArrowCursor)
        self.update_zones_table()
        self.update_image()

    def handle_image_click(self, event):
        """Handle mouse clicks with coordinate conversion for current scale"""
        if not self.original_pixmap:
            return

        click_pos = event.pos()
        displayed_pix = self.image_label.pixmap()
        if not displayed_pix:
            return

        # Calculate image position (centered)
        img_width = displayed_pix.width()
        img_height = displayed_pix.height()
        label_width = self.image_label.width()
        label_height = self.image_label.height()
        
        x_offset = (label_width - img_width) / 2
        y_offset = (label_height - img_height) / 2
        
        # Convert to image coordinates
        img_x = click_pos.x() - x_offset
        img_y = click_pos.y() - y_offset
        
        if 0 <= img_x < img_width and 0 <= img_y < img_height:
            # Convert to original image coordinates
            original_x = img_x * (self.original_pixmap.width() / img_width)
            original_y = img_y * (self.original_pixmap.height() / img_height)
            point = QPoint(int(original_x), int(original_y))
            
            if self.setting_source:
                self.source_point = QPointF(original_x, original_y)
                self.setting_source = False
                self.btn_set_source.setEnabled(False)
                self.btn_add_zone.setEnabled(True)
                self.image_label.setCursor(Qt.ArrowCursor)
            elif self.is_selecting_zone:
                self.current_zone_points.append(point)
                self.btn_finish_zone.setEnabled(len(self.current_zone_points) >= 3)
            
            self.update_image()

    def calculate_polygon_area(self, polygon):
        """Calculate polygon area using shoelace formula (in px²)"""
        area = 0
        n = polygon.size()
        if n < 3:
            return 0
            
        for i in range(n):
            j = (i + 1) % n
            area += polygon.point(i).x() * polygon.point(j).y()
            area -= polygon.point(j).x() * polygon.point(i).y()
            
        return abs(area) / 2

    def update_zones_table(self):
        """Update the zones table with current data"""
        self.zones_table.setRowCount(len(self.selected_zones))
        
        total_pollution_area = pi * (self.outer_radius_m**2 - self.inner_radius_m**2)
        total_defined_area = sum(zone['area'] for zone in self.selected_zones)
        remaining_area = max(0, total_pollution_area - total_defined_area)
        
        # Добавляем строки для определенных зон
        for row, zone in enumerate(self.selected_zones):
            # Тип местности
            self.zones_table.setItem(row, 0, QTableWidgetItem(zone['terrain_type']))
            
            # Площадь в м²
            area_item = QTableWidgetItem()
            area_item.setData(Qt.DisplayRole, f"{zone['area']:,.0f}")
            area_item.setFlags(area_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 1, area_item)
            
            # Показатель относительной опасности
            coeff_item = QTableWidgetItem()
            coeff_item.setData(Qt.DisplayRole, f"{zone['coefficient']:.2f}")
            coeff_item.setFlags(coeff_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 2, coeff_item)
            
            # Доля вклада в %
            contribution = (zone['area'] / total_pollution_area) * 100 if total_pollution_area > 0 else 0
            zone['contribution'] = contribution
            contrib_item = QTableWidgetItem()
            contrib_item.setData(Qt.DisplayRole, f"{contribution:.2f}%")
            contrib_item.setFlags(contrib_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 3, contrib_item)
        
        # Добавляем строку для оставшейся площади (прочие районы)
        if remaining_area > 0:
            row = self.zones_table.rowCount()
            self.zones_table.insertRow(row)
            
            # Тип местности
            self.zones_table.setItem(row, 0, QTableWidgetItem("Прочие районы"))
            
            # Площадь в м²
            area_item = QTableWidgetItem()
            area_item.setData(Qt.DisplayRole, f"{remaining_area:,.0f}")
            area_item.setFlags(area_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 1, area_item)
            
            # Показатель относительной опасности
            coeff_item = QTableWidgetItem()
            coeff_item.setData(Qt.DisplayRole, "0.10")
            coeff_item.setFlags(coeff_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 2, coeff_item)
            
            # Доля вклада в %
            contribution = (remaining_area / total_pollution_area) * 100 if total_pollution_area > 0 else 0
            contrib_item = QTableWidgetItem()
            contrib_item.setData(Qt.DisplayRole, f"{contribution:.2f}%")
            contrib_item.setFlags(contrib_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 3, contrib_item)

    def calculate_damage(self):
        """Calculate economic damage using zone contributions"""
        if not self.source_point:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, сначала установите исходную точку!")
            return
            
        total_pollution_area = pi * (self.outer_radius_m**2 - self.inner_radius_m**2)
        total_defined_area = sum(zone['area'] for zone in self.selected_zones)
        remaining_area = max(0, total_pollution_area - total_defined_area)
        
        # Рассчитываем средневзвешенный коэффициент опасности
        weighted_sum = sum(zone['area'] * zone['coefficient'] for zone in self.selected_zones)
        weighted_sum += remaining_area * 0.1  # Добавляем вклад прочих районов (σ = 0.1)
        
        average_hazard_coefficient = weighted_sum / total_pollution_area if total_pollution_area > 0 else 0

        # Final damage calculation
        economic_damage = (float(self.data['const_to_rubles']) * 
                        average_hazard_coefficient * 
                        self.gross_emission_mass * 
                        float(self.data['deflator']) * 
                        self.popravka_f)

        # Show results with radii information
        result_text = (
            f"<b>Результаты расчета:</b><br><br>"
            f"<b>Площадь зоны активного загрязнения:</b> {total_pollution_area:.0f} м²<br>"
            f"<b>Внутренний радиус:</b> {self.inner_radius_m:.0f} м<br>"
            f"<b>Внешний радиус:</b> {self.outer_radius_m:.0f} м<br><br>"
            f"<b>Определенная площадь:</b> {total_defined_area:.0f} м² ({total_defined_area/total_pollution_area*100:.1f}%)<br>"
            f"<b>Прочие районы:</b> {remaining_area:.0f} м² ({remaining_area/total_pollution_area*100:.1f}%)<br><br>"
            f"<b>Средневзвешенный показатель относительной опасности:</b> {average_hazard_coefficient:.4f}<br><br>"
            f"<b>Экономический ущерб:</b> {economic_damage:.2f} руб./усл.т"
        )
        
        msg = QMessageBox()
        msg.setWindowTitle("Результаты расчета")
        msg.setTextFormat(Qt.RichText)
        msg.setText(result_text)
        
        # Increase the dialog size
        msg.setStyleSheet("QLabel{min-width: 700px; font-size: 12pt;}")
        msg.setMinimumSize(800, 450)
        
        msg.exec_()

    def display_image(self, file_path):
        """Load image and initialize scale"""
        self.original_pixmap = QPixmap(file_path)
        if self.original_pixmap.isNull():
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение карты")
            return
            
        self.update_image()

    def update_image(self):
        """Redraw image with pollution zones for current scale"""
        if not self.original_pixmap:
            return

        # Create temporary pixmap for drawing
        temp_pixmap = QPixmap(self.original_pixmap.size())
        temp_pixmap.fill(Qt.transparent)
        
        painter = QPainter(temp_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 1. Draw original map
        painter.drawPixmap(0, 0, self.original_pixmap)
        
        if self.source_point:
            # 2. Calculate meters-to-pixels ratio
            meters_to_pixels = self.original_pixmap.width() / (1000 * self.current_scale)
            
            # 3. Convert radii from meters to pixels
            inner_px = self.inner_radius_m * meters_to_pixels
            outer_px = self.outer_radius_m * meters_to_pixels
            
            # 4. Draw pollution zones
            painter.setPen(QPen(QColor(255,0,0,80), 2))
            painter.setBrush(QBrush(QColor(255,0,0,30)))
            painter.drawEllipse(self.source_point, outer_px, outer_px)
            
            painter.setPen(QPen(QColor(255,165,0,120), 2))
            painter.setBrush(QBrush(QColor(255,165,0,60)))
            painter.drawEllipse(self.source_point, inner_px, inner_px)
            
            # 5. Draw source point
            painter.setPen(QPen(Qt.black, 3))
            painter.setBrush(QBrush(Qt.red))
            painter.drawEllipse(self.source_point, 5, 5)
            
            # 6. Draw selected zones
            for zone in self.selected_zones:
                painter.setPen(QPen(QColor(0,100,255,150), 2))
                painter.setBrush(QBrush(QColor(0,100,255,80)))
                painter.drawPolygon(zone['polygon'])
            
            # 7. Draw current zone being created
            if self.current_zone_points:
                painter.setPen(QPen(Qt.darkGreen, 2, Qt.DashLine))
                painter.setBrush(Qt.NoBrush)
                for i in range(len(self.current_zone_points) - 1):
                    painter.drawLine(self.current_zone_points[i], self.current_zone_points[i+1])
                if len(self.current_zone_points) > 2:
                    temp_poly = QPolygon(self.current_zone_points)
                    painter.drawPolygon(temp_poly)
        
        painter.end()
        
        # Scale for display
        scaled_pixmap = temp_pixmap.scaled(
            self.image_label.width(),
            self.image_label.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow(None)
    window.show()
    app.exec_()

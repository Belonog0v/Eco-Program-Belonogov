from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QLineEdit, QComboBox, QDialog, QVBoxLayout, QTextEdit, QFileDialog,
                             QWidget, QMessageBox, QHBoxLayout, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, QPolygon, QBrush
from PyQt5.QtCore import Qt, QPoint, QRectF, QPointF
from math import pi, pow, sqrt


class MainWindow(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Основное окно")
        self.setGeometry(100, 100, 800, 720)

        self.label = QLabel("Выберите тип местности", self)
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
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Однородный тип местности")
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
        
        self.hazard_index_input = QLineEdit(self)
        self.hazard_index_input.setGeometry(50, 600, 300, 30)

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
        
        self.emission_clean_factor_label = QLabel("Коэффициент очистки выбросов (F), %", self)
        self.emission_clean_factor_label.setGeometry(375, 300, 400, 30)
        self.emission_clean_factor_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.temperature_mixture_label = QLabel("Температура газо-воздушной смеси, С", self)
        self.temperature_mixture_label.setGeometry(375, 350, 400, 30)
        self.temperature_mixture_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.average_temperature_label = QLabel("Среднегодовая температура атмосферного воздуха, С", self)
        self.average_temperature_label.setGeometry(375, 400, 400, 30)
        self.average_temperature_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.average_wind_label = QLabel("Среднегодовая сила ветра (U), м/с", self)
        self.average_wind_label.setGeometry(375, 450, 400, 30)
        self.average_wind_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.const_to_rubles_label = QLabel("Константа, выраженная в рублях на условную тонну выбросов", self)
        self.const_to_rubles_label.setGeometry(375, 500, 400, 30)
        self.const_to_rubles_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.deflator_label = QLabel("Дефлятор", self)
        self.deflator_label.setGeometry(375, 550, 400, 30)
        self.deflator_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.hazard_index_label = QLabel("Показатель относительной опасности", self)
        self.hazard_index_label.setGeometry(375, 600, 400, 30)
        self.hazard_index_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Кнопки
        self.save_button = QPushButton("Далее", self)
        self.save_button.setFixedSize(200, 50)
        self.save_button.clicked.connect(self.validate_and_save)
        self.save_button.move(510, 650)

        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(200, 50)
        self.back_button.clicked.connect(self.close_first_homogeneous_window)
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
            ('deflator', self.deflator_input, True),
            ('hazard_index', self.hazard_index_input, True)
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
        
        self.new_window = SecondHomogeneousWindow(processed_data)
        self.new_window.show()
        self.close()

    def close_first_homogeneous_window(self):
        self.close()
        self.main_window.show()


class SecondHomogeneousWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.selected_image_path = None  # Добавляем атрибут для хранения пути к изображению
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

        self.image_button = QPushButton("Выбрать изображение", self)
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
            "c = 1 - для всех прочих выбрасываемых в атмосферу загрязнителей (газов, кислот и щелочей в "
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
            "λi = 1,2 - для твердых аэрозолей (пылей), выбрасываемых на территориях со среднегодовым количеством осадков "
            "менее 400 мм в год;\n\n"
            "λi = 1 - для всех остальных случаев."
        )
        lambda_i_dialog = ExplanationDialog(lambda_i_explanation)
        lambda_i_dialog.exec_()

    def show_explain_beta_value(self):
        beta_i_explanation = (
            "Значения поправки β принимаются:\n\n"
            "β = 5 - для нетоксичных летучих углеводородов при поступлении их в атмосферу южнее 40 град. Северной широты;\n\n"
            "β = 2 - для тех же веществ при поступлении их в атмосферу севернее 40 град. Северной широты;\n\n"
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
        self.current_scale = 1.0  # 1x1 km по умолчанию
        self.physical_rect = None
        self.setting_source = False  # Флаг режима установки источника
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Однородный тип местности")
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
        
        self.btn_set_source = QPushButton("Установить источник загрязнения")
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
        
        info_title = QLabel("Результат")
        info_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        self.damage_label = QLabel()
        self.damage_label.setStyleSheet("font-size: 13px; padding: 10px;")
        
        info_layout.addWidget(info_title)
        info_layout.addWidget(self.damage_label)
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
        """Enable source point selection mode"""
        self.setting_source = True
        self.image_label.setCursor(Qt.CrossCursor)
        QMessageBox.information(self, "Исходная точка", 
                              "Нажмите на карту, чтобы установить местоположение источника загрязнения")

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

    def calculate_pollution(self):
        """Recalculate pollution parameters for current scale"""
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
        self.update_damage_label()

    def update_damage_label(self):
        """Update damage information with current scale"""
        self.damage_label.setText(
            f"<b>Масштаб карты:</b> {self.current_scale}x{self.current_scale} км<br>"
            f"<b>Экономический ущерб</b> {self.economic_damage:,.2f} руб./усл. т<br><br>"
            f"<b>Зона загрящнения:</b><br>"
            f"- Внутренний радиус: {self.inner_radius_m:.1f} м<br>"
            f"- Внешний радиус: {self.outer_radius_m:.1f} м"
        )

    def handle_image_click(self, event):
        """Handle mouse clicks with coordinate conversion for current scale"""
        if not self.setting_source or not self.original_pixmap:
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
            
            self.source_point = QPointF(original_x, original_y)
            self.btn_set_source.setEnabled(False)
            self.setting_source = False
            self.image_label.setCursor(Qt.ArrowCursor)
            self.update_image()

    def reset_source_point(self):
        """Reset source point"""
        self.source_point = None
        self.btn_set_source.setEnabled(True)
        self.update_image()

    def display_image(self, file_path):
        """Load image and initialize scale"""
        self.original_pixmap = QPixmap(file_path)
        if self.original_pixmap.isNull():
            QMessageBox.warning(self, "Error", "Failed to load map image")
            return
            
        self.update_image()

    def update_image(self):
        """Redraw image with pollution zones for current scale"""
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
        
        self.hazard_index_input = QLineEdit(self)
        self.hazard_index_input.setGeometry(50, 600, 300, 30)

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
        
        self.emission_clean_factor_label = QLabel("Коэффициент очистки выбросов (F), %", self)
        self.emission_clean_factor_label.setGeometry(375, 300, 400, 30)
        self.emission_clean_factor_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.temperature_mixture_label = QLabel("Температура газо-воздушной смеси, С", self)
        self.temperature_mixture_label.setGeometry(375, 350, 400, 30)
        self.temperature_mixture_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.average_temperature_label = QLabel("Среднегодовая температура атмосферного воздуха, С", self)
        self.average_temperature_label.setGeometry(375, 400, 400, 30)
        self.average_temperature_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.average_wind_label = QLabel("Среднегодовая сила ветра (U), м/с", self)
        self.average_wind_label.setGeometry(375, 450, 400, 30)
        self.average_wind_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.const_to_rubles_label = QLabel("Константа, выраженная в рублях на условную тонну выбросов", self)
        self.const_to_rubles_label.setGeometry(375, 500, 400, 30)
        self.const_to_rubles_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.deflator_label = QLabel("Дефлятор", self)
        self.deflator_label.setGeometry(375, 550, 400, 30)
        self.deflator_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.hazard_index_label = QLabel("Показатель относительной опасности", self)
        self.hazard_index_label.setGeometry(375, 600, 400, 30)
        self.hazard_index_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

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
            ('deflator', self.deflator_input, True),
            ('hazard_index', self.hazard_index_input, True)
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

        self.image_button = QPushButton("Выбрать изображение", self)
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
            "c = 1 - для всех прочих выбрасываемых в атмосферу загрязнителей (газов, кислот и щелочей в "
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
            "λi = 1,2 - для твердых аэрозолей (пылей), выбрасываемых на территориях со среднегодовым количеством осадков "
            "менее 400 мм в год;\n\n"
            "λi = 1 - для всех остальных случаев."
        )
        lambda_i_dialog = ExplanationDialog(lambda_i_explanation)
        lambda_i_dialog.exec_()

    def show_explain_beta_value(self):
        beta_i_explanation = (
            "Значения поправки β принимаются:\n\n"
            "β = 5 - для нетоксичных летучих углеводородов при поступлении их в атмосферу южнее 40 град. Северной широты;\n\n"
            "β = 2 - для тех же веществ при поступлении их в атмосферу севернее 40 град. Северной широты;\n\n"
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
        self.current_scale = 1.0  # 1x1 км по умолчанию
        self.physical_rect = None
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Неоднородный тип местности")
        self.setGeometry(100, 100, 1200, 850)

        # Main layout
        layout = QVBoxLayout()

        # Header with scale selection
        header = QWidget()
        header_layout = QHBoxLayout(header)
        
        scale_label = QLabel("Map Scale:")
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
        self.image_label.setMinimumSize(800, 600)
        self.image_label.setStyleSheet("border: 2px solid #ccc; background: #f8f8f8;")
        self.image_label.mousePressEvent = self.handle_image_click
        image_layout.addWidget(self.image_label)

        # Image controls
        controls_widget = QWidget()
        controls_layout = QHBoxLayout(controls_widget)
        
        self.btn_set_source = QPushButton("Установить источник загрязнения")
        self.btn_set_source.clicked.connect(self.enable_source_selection)
        
        self.btn_add_zone = QPushButton("Добавить зону")
        self.btn_add_zone.setEnabled(False)
        self.btn_add_zone.clicked.connect(self.start_zone_selection)
        
        self.btn_finish_zone = QPushButton("Сохранить зону")
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

        # Zones panel (30%)
        zones_widget = QWidget()
        zones_layout = QVBoxLayout(zones_widget)
        
        zones_title = QLabel("Управление зонами")
        zones_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        self.zones_table = QTableWidget()
        self.zones_table.setColumnCount(4)
        self.zones_table.setHorizontalHeaderLabels(["Зона", "Площадь (м²)", "Значение относительной опасности", "Вклад"])
        self.zones_table.setColumnWidth(0, 60)
        self.zones_table.setColumnWidth(1, 100)
        self.zones_table.setColumnWidth(2, 100)
        self.zones_table.setColumnWidth(3, 120)
        
        self.btn_calculate = QPushButton("Рассчитать")
        self.btn_calculate.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 8px;")
        self.btn_calculate.clicked.connect(self.calculate_damage)
        
        zones_layout.addWidget(zones_title)
        zones_layout.addWidget(self.zones_table)
        zones_layout.addWidget(self.btn_calculate)

        # Add to content layout
        content_layout.addWidget(image_widget, 70)
        content_layout.addWidget(zones_widget, 30)

        # Add to main layout
        layout.addWidget(content_widget)
        self.setLayout(layout)

        # Initial setup
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

    def enable_source_selection(self):
        """Enable source point selection mode"""
        self.setting_source = True
        self.image_label.setCursor(Qt.CrossCursor)
        QMessageBox.information(self, "Исходная точка", 
                              "Нажмите на карту, чтобы установить местоположение источника загрязнения")

    def start_zone_selection(self):
        """Begin zone creation mode"""
        if not self.source_point:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, сначала установите исходную точку!")
            return
            
        self.is_selecting_zone = True
        self.current_zone_points = []
        self.image_label.setCursor(Qt.CrossCursor)
        self.btn_finish_zone.setEnabled(False)
        QMessageBox.information(self, "Создание зоны", 
                                    "Нажмите на карту, чтобы добавить вершины зоны\n"
                                    "Требуется минимум 3 точки\n"
                                    "Нажмите 'Завершить зону', когда закончите")

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
        
        self.selected_zones.append({
            'polygon': polygon,
            'area': actual_area,
            'coefficient': 1.0,  # Default coefficient
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
        
        total_area = pi * (self.outer_radius_m**2 - self.inner_radius_m**2)
        
        for row, zone in enumerate(self.selected_zones):
            # Zone number
            self.zones_table.setItem(row, 0, QTableWidgetItem(f"Зона {row+1}"))
            
            # Area in m²
            area_item = QTableWidgetItem()
            area_item.setData(Qt.DisplayRole, f"{zone['area']:.0f}")
            area_item.setFlags(area_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 1, area_item)
            
            # Coefficient (editable)
            coeff_item = QTableWidgetItem()
            coeff_item.setData(Qt.DisplayRole, f"{zone['coefficient']:.2f}")
            self.zones_table.setItem(row, 2, coeff_item)
            
            # Contribution (calculated)
            contribution = (zone['area'] / total_area) * zone['coefficient'] if total_area > 0 else 0
            zone['contribution'] = contribution
            contrib_item = QTableWidgetItem()
            contrib_item.setData(Qt.DisplayRole, f"{contribution:.4f}")
            contrib_item.setFlags(contrib_item.flags() ^ Qt.ItemIsEditable)
            self.zones_table.setItem(row, 3, contrib_item)

    def calculate_damage(self):
        """Calculate economic damage using zone contributions"""
        if not self.source_point:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, сначала установите исходную точку!")
            return
            
        if not self.selected_zones:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, добавьте хотя бы одну зону!")
            return

        # Update coefficients from table
        total_contribution = 0
        total_area = pi * (self.outer_radius_m**2 - self.inner_radius_m**2)
        
        for row in range(self.zones_table.rowCount()):
            try:
                coeff = float(self.zones_table.item(row, 2).text())
                self.selected_zones[row]['coefficient'] = coeff
                
                # Recalculate contribution
                zone_area = self.selected_zones[row]['area']
                contribution = (zone_area / total_area) * coeff if total_area > 0 else 0
                self.selected_zones[row]['contribution'] = contribution
                total_contribution += contribution
                
                # Update table
                self.zones_table.item(row, 3).setText(f"{contribution:.4f}")
            except ValueError:
                QMessageBox.warning(self, "Ошибка", f"Неверный коэффициент в строке {row+1}")
                return

        # Calculate hazard index based on zones
        hazard_index = float(self.data['hazard_index']) * total_contribution
        
        # Final damage calculation
        economic_damage = (float(self.data['const_to_rubles']) * 
                         hazard_index * 
                         self.gross_emission_mass * 
                         float(self.data['deflator']) * 
                         self.popravka_f)

        # Show results
        result_text = (
            f"<b>Результат:</b><br><br>"
            f"Масштаб карты: {self.current_scale}x{self.current_scale} км<br>"
            f"Всего зон: {len(self.selected_zones)}<br>"
            f"Скорректированный индекс опасности: {hazard_index:.2f}<br><br>"
            f"<b>Окончательный экономический ущерб: {economic_damage:,.2f} руб./усл.т</b><br><br>"
        )
        
        msg = QMessageBox()
        msg.setWindowTitle("Рассчитать")
        msg.setTextFormat(Qt.RichText)
        msg.setText(result_text)
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

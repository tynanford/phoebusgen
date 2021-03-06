import os


class GenericTest(object):
    def test_basics(self):
        self.assertEqual(self.element.get_element_value('name'), self.name)
        self.assertEqual(self.element.get_element_value('x'), str(self.x))
        self.assertEqual(self.element.get_element_value('y'), str(self.y))
        self.assertEqual(self.element.get_element_value('width'), str(self.width))
        self.assertEqual(self.element.get_element_value('height'), str(self.height))

    def test_against_file(self):
        curr_path = os.path.dirname(__file__)
        try:
            open(curr_path + '../files/widgets/{}.bob'.format(self.element.root.attrib['type']))
        except FileNotFoundError:
            print('File Not there!')
            return
        with open(curr_path + '/../files/widgets/{}.bob'.format(self.element.root.attrib['type'])) as f:
            xml = f.read()
            self.assertEqual(xml, self.element.prettify(self.element.root))

    def generic_element_test(self, tag_name, value):
        element = self.element.find_element(tag_name)
        self.assertFalse(isinstance(element, list))
        self.assertIsNotNone(element)
        if value is None:
            self.assertIsNone(element.text)
        else:
            if type(value) == bool:
                self.assertEqual(element.text, str(value).lower())
            else:
                self.assertEqual(element.text, str(value))
        self.element.remove_element(tag_name)
        self.assertIsNone(self.element.find_element(tag_name))

    def null_test(self, tag_name):
        self.assertIsNone(self.element._prop_factory.root.find(tag_name))

    def child_element_test(self, parent_tag, tag_name, value, attrib):
        parent = self.element.find_element(parent_tag)
        self.assertIsNotNone(parent)
        child = parent.find(tag_name)
        self.assertIsNotNone(child)
        if value is None:
            self.assertIsNone(child.text)
        else:
            self.assertEqual(child.text, str(value))
        self.assertEqual(child.attrib, attrib)

        self.element.remove_element(parent_tag)
        self.assertIsNone(self.element.find_element(parent_tag))


class TestPVName(GenericTest):
    def test_pv_name(self):
        self.assertEqual(self.element.find_element('pv_name').text, self.pv_name)


class TestText(GenericTest):
    def test_text(self):
        self.assertEqual(self.element.find_element('text').text, self.text)


class TestFont(GenericTest):
    def test_predefined_font(self):
        tag_name = 'font'
        self.element.font()
        self.child_element_test(tag_name, 'font', None, {'family': 'Liberation Sans', 'size': '14', 'style': 'Regular'})

    def test_font(self):
        tag_name = 'font'
        value = 'Header 1'
        self.element.predefined_font(value)
        self.child_element_test(tag_name, 'font', None, {'family': 'Liberation Sans', 'size': '22', 'style': 'Bold'})


class TestForegroundColor(GenericTest):
    def test_predefined_foreground_color(self):
        tag_name = 'foreground_color'
        value = 'Background'
        self.element.predefined_foreground_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_foreground_color(self):
        tag_name = 'foreground_color'
        self.element.foreground_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})


class TestBackgroundColor(GenericTest):
    def test_predefined_background_color(self):
        tag_name = 'background_color'
        value = 'MINOR'
        self.element.predefined_background_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'MINOR', 'red': '255', 'green': '128', 'blue': '0', 'alpha': '255'})

    def test_background_color(self):
        tag_name = 'background_color'
        self.element.background_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10', 'blue': '15', 'alpha': '255'})


class TestTransparent(GenericTest):
    def test_transparent(self):
        tag_name = 'transparent'
        value = True
        self.element.transparent(value)
        self.generic_element_test(tag_name, value)


class TestFormat(GenericTest):
    def test_format(self):
        tag_name = 'format'
        value = 'Engineering'
        xml_value = '3'
        self.element.format(value)
        self.generic_element_test(tag_name, xml_value)


class TestPrecision(GenericTest):
    def test_precision(self):
        tag_name = 'precision'
        value = 25.3
        real_value = '25'
        self.element.precision(value)
        self.generic_element_test(tag_name, real_value)


class TestShowUnits(GenericTest):
    def test_show_units(self):
        tag_name = 'show_units'
        value = False
        self.element.show_units(value)
        self.generic_element_test(tag_name, value)


class TestHorizontalAlignment(GenericTest):
    def test_horizontal_alignment(self):
        tag_name = 'horizontal_alignment'
        value = 'Center'
        xml_value = 1
        self.element.horizontal_alignment(value)
        self.generic_element_test(tag_name, xml_value)


class TestVerticalAlignment(GenericTest):
    def test_vertical_alignment(self):
        tag_name = 'vertical_alignment'
        value = 'Middle'
        xml_value = 1
        self.element.vertical_alignment(value)
        self.generic_element_test(tag_name, xml_value)


class TestWrapWords(GenericTest):
    def test_wrap_words(self):
        tag_name = 'wrap_words'
        value = False
        self.element.wrap_words(value)
        self.generic_element_test(tag_name, value)


class TestRotationStep(GenericTest):
    def test_rotation_step(self):
        tag_name = 'rotation_step'
        value = 180
        xml_value = 2
        self.element.rotation_step(value)
        self.generic_element_test(tag_name, xml_value)


class TestBorder(GenericTest):
    def test_border_width(self):
        tag_name = 'border_width'
        value = 2
        self.element.border_width(value)
        self.generic_element_test(tag_name, value)

    def test_border_color(self):
        tag_name = 'border_color'
        self.element.border_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10', 'blue': '15', 'alpha': '255'})

    def test_predefined_border_color(self):
        tag_name = 'border_color'
        value = 'Attention'
        self.element.predefined_border_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'Attention', 'red': '255', 'green': '160',
                                                          'blue': '0', 'alpha': '255'})


class TestMacro(GenericTest):
    def test_macro(self):
        self.element.macro('test', 'mac1')
        self.child_element_test('macros', 'test', 'mac1', {})


class TestBit(GenericTest):
    tag_name = 'bit'

    def test_bit_with_number(self):
        value = 234
        self.element.bit(value)
        self.generic_element_test(self.tag_name, value)

    def test_default_bit(self):
        self.element.bit()
        self.generic_element_test(self.tag_name, -1)


class TestAutoSize(GenericTest):

    def test_auto_size(self):
        tag_name = 'auto_size'
        val = False
        self.element.auto_size(val)
        self.generic_element_test(tag_name, val)

    def test_auto_size_default(self):
        tag_name = 'auto_size'
        self.element.auto_size()
        self.generic_element_test(tag_name, True)


class TestMultiLine(GenericTest):
    def test_multi_line(self):
        tag_name = 'multi_line'
        val = True
        self.element.multi_line(val)
        self.generic_element_test(tag_name, val)


class TestSquare(GenericTest):
    def test_square(self):
        tag_name = 'square'
        val = True
        self.element.square(val)
        self.generic_element_test(tag_name, val)


class TestLabelsFromPV(GenericTest):
    def test_labels_from_pv(self):
        tag_name = 'labels_from_pv'
        val = True
        self.element.labels_from_pv(val)
        self.generic_element_test(tag_name, val)


class TestAlarmBorder(GenericTest):
    def test_alarm_border(self):
        tag_name = 'border_alarm_sensitive'
        val = True
        self.element.alarm_border(val)
        self.generic_element_test(tag_name, val)


class TestEnabled(GenericTest):
    def test_enabled(self):
        tag_name = 'enabled'
        val = False
        self.element.enabled(val)
        self.generic_element_test(tag_name, val)


class TestLineWidth(GenericTest):
    tag_name = 'line_width'

    def test_line_width(self):
        val = 5
        self.element.line_width(val)
        self.generic_element_test(self.tag_name, val)

    def test_line_width_wrong(self):
        val = 'asdfs'
        self.element.line_width(val)
        self.null_test(self.tag_name)


class TestCorner(GenericTest):
    def test_corner_width(self):
        tag_name = 'corner_width'
        val = 5
        self.element.corner_width(val)
        self.generic_element_test(tag_name, val)

    def test_corner_width_string(self):
        tag_name = 'corner_width'
        val = 'asdjflksdjf'
        self.element.corner_width(val)
        self.null_test(tag_name)

    def test_corner_height(self):
        tag_name = 'corner_height'
        val = 5
        self.element.corner_height(val)
        self.generic_element_test(tag_name, val)

    def test_corner_height_string(self):
        tag_name = 'corner_height'
        val = 'asdjflksdjf'
        self.element.corner_height(val)
        self.null_test(tag_name)


class TestAngle(GenericTest):
    def test_angle_start(self):
        tag_name = 'start_angle'
        val = 32
        self.element.angle_start(val)
        self.generic_element_test(tag_name, val)

    def test_angle_size(self):
        tag_name = 'total_angle'
        val = 92
        self.element.angle_size(val)
        self.generic_element_test(tag_name, val)


class TestConfirmation(GenericTest):
    dialog_tag = 'show_confirmation_dialog'
    message_tag = 'confirm_message'
    password_tag = 'password'
    message = 'Are you sure?'

    def test_confirmation_no_password(self):
        self.element.confirmation_dialog(self.message)
        self.generic_element_test(self.message_tag, self.message)
        self.generic_element_test(self.dialog_tag, True)
        self.null_test(self.password_tag)
        self.null_test(self.password_tag)

    def test_confirmation_with_password(self):
        password = '1234569999'
        self.element.confirmation_dialog(self.message, password)
        self.generic_element_test(self.message_tag, self.message)
        self.generic_element_test(self.dialog_tag, True)
        self.generic_element_test(self.password_tag, password)


class TestLineColor(GenericTest):
    def test_predefined_line_color(self):
        tag_name = 'line_color'
        value = 'Background'
        self.element.predefined_line_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_line_color(self):
        tag_name = 'line_color'
        self.element.line_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})


class TestOffColor(GenericTest):
    def test_predefined_off_color(self):
        tag_name = 'off_color'
        value = 'Background'
        self.element.predefined_off_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_off_color(self):
        tag_name = 'off_color'
        self.element.off_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

class TestOff(TestOffColor):
    def test_off_label(self):
        tag_name = 'off_label'
        value = 'This is off!'
        self.element.off_label(value)
        self.generic_element_test(tag_name, value)

class TestOnColor(GenericTest):
    def test_predefined_on_color(self):
        tag_name = 'on_color'
        value = 'Background'
        self.element.predefined_on_color(value)
        self.child_element_test(tag_name, 'color', None, {'name': 'Background', 'red': '255', 'green': '255',
                                                          'blue': '255', 'alpha': '255'})

    def test_on_color(self):
        tag_name = 'on_color'
        self.element.on_color(5, 10, 15)
        self.child_element_test(tag_name, 'color', None, {'red': '5', 'green': '10',
                                                          'blue': '15', 'alpha': '255'})

class TestOn(TestOnColor):
    def test_on_label(self):
        tag_name = 'on_label'
        value = 'This is on!'
        self.element.on_label(value)
        self.generic_element_test(tag_name, value)

class TestStretchToFit(GenericTest):
    def test_stretch_to_fit1(self):
        tag_name = 'stretch_image'
        val = False
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, val)

    def test_stretch_to_fit2(self):
        tag_name = 'stretch_image'
        val = 'false'
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, False)

    def test_stretch_to_fit3(self):
        tag_name = 'stretch_image'
        val = True
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, val)

    def test_stretch_to_fit4(self):
        tag_name = 'stretch_image'
        val = 1
        self.element.stretch_to_fit(val)
        self.generic_element_test(tag_name, True)


class TestFile(GenericTest):
    # file is a constructor param for widgets (similar to x or pv_name)
    # so we don't have to add it here, just test that it made it
    def test_file(self):
        tag_name = 'file'
        self.generic_element_test(tag_name, self.file)


class TestRotation(GenericTest):
    tag_name = 'rotation'

    def test_rotation1(self):
        val = 24
        self.element.rotation(val)
        self.generic_element_test(self.tag_name, val)

    def test_rotation2(self):
        val = -12.2
        self.element.rotation(val)
        self.generic_element_test(self.tag_name, val)

    def test_rotation3(self):
        val = 142.2
        self.element.rotation(val)
        self.generic_element_test(self.tag_name, val)

    def test_rotation4(self):
        val = 'sadfdsf'
        self.element.rotation(val)
        self.null_test(self.tag_name)


class TestResizeBehavior(GenericTest):
    tag_name = 'resize'
    def test_default(self):
        self.generic_element_test(self.tag_name, 0)

    def test_no_resize(self):
        self.element.no_resize()
        self.generic_element_test(self.tag_name, 0)

    def test_size_content_to_fit_widget(self):
        self.element.size_content_to_fit_widget()
        self.generic_element_test(self.tag_name, 1)

    def test_size_widget_to_match_content(self):
        self.element.size_widget_to_match_content()
        self.generic_element_test(self.tag_name, 2)


    def test_stretch_content_to_fit_widget(self):
        self.element.stretch_content_to_fit_widget()
        self.generic_element_test(self.tag_name, 3)

    def test_crop_content(self):
        self.element.crop_content()
        self.generic_element_test(self.tag_name, 4)


class TestGroupName(GenericTest):
    # we should be able to add property multiple times, with only the latest being added to xml
    def test_add_twice(self):
        tag_name = 'group_name'
        val = 'test2'
        self.element.group_name('test')
        self.element.group_name(val)
        self.generic_element_test(tag_name, val)

class TestStyle(GenericTest):
    def test_default(self):
       self.generic_element_test('style', 0)

    def test_add_elem_twice(self):
        self.element.group_box()
        self.generic_element_test('style', 0)

    def test_title_bar(self):
        self.element.title_bar()
        self.generic_element_test('style', 1)

    def test_line(self):
        self.element.line()
        self.generic_element_test('style', 2)

    def test_no_style(self):
        self.element.no_style()
        self.generic_element_test('style', 3)


class TestLabel(GenericTest):
    def test_label(self):
        tag_name = 'label'
        self.generic_element_test(tag_name, self.label)

class TestItemsFromPV(GenericTest):
    def test_default(self):
        tag_name = 'items_from_pv'
        self.generic_element_test(tag_name, True)

    def test_off(self):
        tag_name = 'items_from_pv'
        self.element.items_from_pv(False)
        self.generic_element_test(tag_name, False)

class TestItems(GenericTest):
    def test_add_item(self):
        tag_name = 'items'
        val = 'Item Number Uno'
        self.element.item(val)
        self.child_element_test(tag_name, 'item', val, {})

class TestActions(GenericTest):
    def test_execute_as_one(self):
        tag_name = 'actions'
        self.element.action_execute_as_one(True)
        file = 'test.bob'
        target = 'TaB'
        self.element.action_open_display(file, target)
        self.child_element_test(tag_name, 'action', None, {'type': 'open_display'})

    # need to get child test for child of child to work
    #def test_open_display(self):
    #    tag_name = 'action'
    #    file = 'test.bob'
    #    target = 'TaB'
    #    self.element.action_open_display(file, target)
    #    print(self.element)
    #    self.child_element_test(tag_name, 'description', 'Open Display', {})



class TestHorizontal(GenericTest):
    def test_default(self):
        tag_name = 'horizontal'
        self.generic_element_test(tag_name, True)

    def test_off(self):
        tag_name = 'horizontal'
        self.element.horizontal(False)
        self.generic_element_test(tag_name, False)

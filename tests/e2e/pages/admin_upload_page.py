from .base_page import BasePage

class AdminUploadPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.file_input = 'input[type="file"]'
        self.upload_btn = 'button:has-text("Continuar para Mapeamento")'
        self.project_name_input = 'input[name="project_name"]'
        self.select_area = 'select[name="mapping_area"]'
        self.select_subarea = 'select[name="mapping_subarea"]'
        self.select_disciplina = 'select[name="mapping_disciplina"]'
        self.process_btn = 'button:has-text("Processar XML")'
        self.success_msg = '.alert-success'

    def upload_xml(self, file_path):
        self.page.locator(self.file_input).set_input_files(file_path)
        self.page.wait_for_load_state("networkidle")
        self.click(self.upload_btn)
        self.page.wait_for_selector(self.project_name_input)

    def fill_mapping(self, project_name, mapping_dict):
        self.fill(self.project_name_input, project_name)
        if 'area' in mapping_dict:
            self.page.select_option(self.select_area, value=mapping_dict['area'])
        if 'subarea' in mapping_dict:
            self.page.select_option(self.select_subarea, value=mapping_dict['subarea'])
        if 'disciplina' in mapping_dict:
            self.page.select_option(self.select_disciplina, value=mapping_dict['disciplina'])
        self.click(self.process_btn)

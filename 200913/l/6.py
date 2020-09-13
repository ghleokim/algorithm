class Applicant:
    def __init__(self, company, max_num):
        self.company = list(company)
        self.stat = 0
        self.max_num = max_num


class Company:
    def __init__(self, applicant, max_num):
        self.applicant = list(applicant)
        self.stat = 0
        self.max_num = max_num


def solution(companies, applicants):
    answer = []

    app_dict = {}

    for app in applicants:
        person, company, max_num = app.split()
        app_dict[person] = Applicant(company, max_num)

    for app in app_dict.keys():
        print(app, app_dict[app].company, app_dict[app].max_num)

    comp_dict = {}

    for comp in companies:
        company, applicant, max_num = comp.split()
        comp_dict[company] = Company(applicant, max_num)

    for comp in comp_dict.keys():
        print(comp, comp_dict[comp].applicant, comp_dict[comp].max_num)

    for rnd in range(4):
        rnd_apply = {}
        res_apply = {}
        for comp in comp_dict.keys():
            rnd_apply[comp] = []
            res_apply[comp] = []
        for app in app_dict.keys():
            if app_dict[app].stat <= app_dict[app].max_num:
                target = app_dict[app].company[app_dict[app].stat]
                rnd_apply[target].append(app)
                app.stat += 1
        
        for comp in comp_dict.keys():
            cur_apply = rnd_apply[comp]

            cur_max = comp_dict[comp].max_num
            
            cur_apply.sort(key=comp_dict[comp].applicant)
            
            if len(cur_apply) < cur_max:
                cu

    return answer

solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"],["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"])
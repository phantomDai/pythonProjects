"""
get all residual mutants
"""

import xlrd
import os
import matplotlib.pyplot as plt

"""
read one files of any object, obtain killed mutants
"""
def read_excel(path):
    workbook = xlrd.open_workbook(path, encoding_override='utf-8')
    """create a set"""
    result = set()
    """traverse each sheet"""
    for i in range(0, 5):
        sheet = workbook.sheet_by_index(i)
        rows = sheet.nrows
        """get killed mutants"""
        for j in range(1, rows):
            temp_str = sheet.cell(j, 4).value

            if temp_str.strip() == '':
                continue
            elements = temp_str.split(';')

            for element in elements:
                if element.strip() == '':
                    continue
                result.add(element)
    return result


"""
read all files of a object, and then obtain all killed mutants
"""
def read_all_mutants_files(object_name):
    """obtain the resulting path of the specified object"""
    path = os.path.abspath(os.path.join(os.getcwd(), "..", "excels", object_name))

    """create a set that includes all killed mutants"""
    result = set()

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        temp_result = read_excel(file_path)
        for element in temp_result:
            result.add(element)

    return result


"""read scenario-base files that includes all mutants of the specified object"""
def read_mutantinfo(object_name, scenario):
    mutants_info = os.path.abspath(os.path.join(os.getcwd(), "..", "mutantinfo", object_name, scenario))

    """create a set that include all mutants of scenario"""
    result = set()

    """traverse the mutantinfo text file"""
    for line in open(mutants_info, 'r'):
        result.add(line.rstrip("\n"))

    return result


"""get difference set by comparing the killed-mutant set and mutantInfo set"""
def compare_two_sets(result, mutant_info):
    difference_set = set(result)^set(mutant_info)
    return difference_set


"""write the result of different scenarios"""
def write_reslut_to_statistic_result(difference_set, path):
    log = "the difference set is:" + ''.join(difference_set) + "\n" + \
          "the length of this set is:" + str(len(difference_set))
    with open(path, 'a+') as fw:
        fw.write(log)
    fw.close()


"""write results to a file"""
def write_results_to_file():
    objects = ["SimpleLinear", "SimpleTree", "SequentialHeap", "FineGrainedHeap", "SkipQueue"]

    for object in objects:
        killedmutants = read_all_mutants_files(object)
        mutantsinfo = read_mutantinfo(object, "sequentialAndsequential")
        differenceSet = compare_two_sets(killedmutants, mutantsinfo)
        path = os.path.abspath(os.path.join(os.getcwd(), "..", "statisticResult", "allScenarios", object))
        write_reslut_to_statistic_result(differenceSet, path)

    """write the scenarios results"""
    scenarios = ["concurrentAndconcurrent", "concurrentAndsequential",
                 "sequentialAndconcurrent", "sequentialAndsequential"]

    for scenario in scenarios:
        for object in objects:
            killedmutants = read_mutantinfo(object, scenario)
            mutantsinfo = read_mutantinfo(object, scenario)
            differenceSet = compare_two_sets(killedmutants, mutantsinfo)
            path = os.path.abspath(os.path.join(os.getcwd(), "..", "statisticResult", "oneScenario", object + "_" + scenario))
            write_reslut_to_statistic_result(differenceSet, path)






if __name__ == '__main__':
    write_results_to_file()

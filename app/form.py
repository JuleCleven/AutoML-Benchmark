from app import app
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AutoML.db'
db = SQLAlchemy(app)


class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    payment = db.Column(db.Boolean)
    programming_skills = db.Column(db.Boolean)  # Are Basic Programming skills required?
    datascience_skills = db.Column(db.Boolean)
    python = db.Column(db.Boolean)  # programming languages
    java = db.Column(db.Boolean)
    r = db.Column(db.Boolean)
    scala = db.Column(db.Boolean)
    cloud_computing = db.Column(db.Boolean)
    linux = db.Column(db.Boolean)  # table for os?
    mac_os = db.Column(db.Boolean)
    windows = db.Column(db.Boolean)

    automatic = db.Column(db.Boolean)
    numerical = db.Column(db.Boolean)  # input datatypes 'table for it ?
    time_series = db.Column(db.Boolean)
    images = db.Column(db.Boolean)
    videos = db.Column(db.Boolean)
    audios = db.Column(db.Boolean)
    text = db.Column(db.Boolean)

    input_required = db.Column(db.String(50))
    handling_missing_values = db.Column(db.Boolean)
    outliers_detection_deletion = db.Column(db.Boolean)
    data_standardization = db.Column(db.Boolean)
    data_encoding = db.Column(db.Boolean)
    feature_scaling = db.Column(db.Boolean)
    data_reduction = db.Column(db.Boolean)
    data_balancing = db.Column(db.Boolean)
    data_augmentation = db.Column(db.Boolean)
    feature_generation = db.Column(db.Boolean)
    integrated_modeling = db.Column(db.Boolean)

    training = db.Column(db.Boolean)
    ml_algorithms_included = db.Column(db.Boolean)  # algorithms table ?
    decision_tree = db.Column(db.Boolean)
    gaussian_processes = db.Column(db.Boolean)
    annealing = db.Column(db.Boolean)
    tree_of_parzen_estimators = db.Column(db.Boolean)
    light_gbm = db.Column(db.Boolean)
    random_search = db.Column(db.Boolean)
    adaboost = db.Column(db.Boolean)
    gradient_boosting = db.Column(db.Boolean)
    logistic_regression = db.Column(db.Boolean)
    knn = db.Column(db.Boolean)
    random_forest = db.Column(db.Boolean)
    svm = db.Column(db.Boolean)
    xgboost = db.Column(db.Boolean)
    neural_network = db.Column(db.Boolean)
    regression = db.Column(db.Boolean)
    xgboost_gb = db.Column(db.Boolean)
    k_nearest_neighbors = db.Column(db.Boolean)
    regularized_greedy_forest = db.Column(db.Boolean)
    extra_trees = db.Column(db.Boolean)
    deep_neural_network = db.Column(db.Boolean)
    anti_overfitting_approach = db.Column(db.Boolean)  # crossvalidtaion = True
    evaluation_approach = db.Column(db.Boolean)
    search = db.Column(db.String(20))
    gui = db.Column(db.Boolean)
    hyperparameter_selection = db.Column(db.Boolean)
    metrics = db.Column(db.Boolean)
    charts = db.Column(db.Boolean)

    # productionize_model = db.Column(db.String(50))
    web_service = db.Column(db.Boolean)
    online_model_training = db.Column(db.Boolean)

    preliminary_results = db.Column(db.Boolean)
    best_model = db.Column(db.Boolean)  # final results
    evaluation = db.Column(db.Boolean)
    ensamble = db.Column(db.Boolean)
    model_characteristics = db.Column(db.Boolean)
    leaderboard = db.Column(db.Boolean)
    written_reports = db.Column(db.Boolean)
    feature_matrix = db.Column(db.Boolean)


db.create_all()


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/process', methods=['POST'])
def process():
    user_info = {}  # information about the choices of the user
    crit_info = {}  # information about the choices of the user
    crit = {}  # information about the compatibility of the system and user
    score = {}  # information about the compatibility of the system and user
    answercount = 0
    systems = System.query.all()
    for system in systems:
        score[system] = 0
        crit[system] = False

    request_keys = []
    for c in System.__table__.columns.keys():
        request_keys.append(c)
    request_keys.pop(0)
    request_keys.pop(0)

    crit_keys = ['crit_payment', 'crit_programming_skills', 'crit_datascience_skills', 'crit_prog_lang',
                 'crit_prog_lang', 'crit_prog_lang', 'crit_prog_lang', 'crit_cloud_computing', 'crit_os', 'crit_os',
                 'crit_os', 'crit _automatic', 'crit_data_types', 'crit_data_types', 'crit_data_types',
                 'crit_data_types', 'crit_data_types', 'crit_data_types', 'crit_input', 'crit_processing',
                 'crit_processing',
                 'crit_processing', 'crit_processing', 'crit_processing', 'crit_processing', 'crit_processing',
                 'crit_processing', 'crit_feature_engineering', 'crit_feature_engineering', 'crit_training',
                 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms',
                 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms',
                 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms',
                 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms',
                 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms', 'crit_ml_algorithms',
                 'crit_ml_algorithms', 'crit_anti_overfitting_approach', 'crit_evaluation_approach', 'crit_search',
                 'crit_gui',
                 'crit_hyper_selection', 'crit_metrics', 'crit_charts', 'crit_web_service',
                 'crit_online_model_training',
                 'crit_pre-results', 'crit_results', 'crit_results', 'crit_results', 'crit_results', 'crit_results',
                 'crit_results', 'crit_results']

    def get_user_info(request_keys, crit_keys):
        for k in request_keys:
            user_info[k] = request.form.get(k)
        for k in crit_keys:
            crit_info[k] = request.form.get(k)
        info = {'user_info': user_info, 'crit_info': crit_info}
        return info

    # print(request.get_data())
    # for k in user_info:
    #     if user_info[k] == 'True':
    #         answercount = answercount + 1
    #
    #     if user_info[k] == 'False':
    #         answercount = answercount + 1
    # answercount = request.get_data().count("True") + request.get_data().count("False")
    response = get_user_info(request_keys, crit_keys)

    # print(response)

    def parse_response(response):
        user_info = response['user_info']
        for k in user_info:
            if user_info[k] == 'True':
                user_info[k] = True
            if user_info[k] == 'False':
                user_info[k] = False

        crit_info = response['crit_info']
        for k in crit_info:
            if crit_info[k] == 'True':
                crit_info[k] = True

        info = {'user_info': user_info, 'crit_info': crit_info}

        return info

    parsed_response = parse_response(response)

    crit_info = parsed_response['crit_info']
    user_info = parsed_response['user_info']
    # print(crit_info)
    # print(user_info)

    request_columns = ['payment', 'programming_skills', 'datascience_skills', 'python', 'r', 'java', 'scala',
                       'cloud_computing', 'linux', 'mac_os', 'windows', 'automatic', 'numerical', 'time_series',
                       'images', 'videos', 'audios', 'text', 'input_required', 'handling_missing_values',
                       'outliers_detection_deletion', 'data_standardization', 'data_encoding', 'feature_scaling',
                       'data_reduction', 'data_balancing', 'data_augmentation', 'feature_generation',
                       'integrated_modeling', 'training', 'anti_overfitting_approach', 'evaluation_approach',
                       'search', 'gui', 'hyperparameter_selection', 'metrics', 'charts', 'web_service',
                       'online_model_training', 'preliminary_results', 'best_model', 'evaluation', 'ensamble',
                       'leaderboard', 'model_characteristics', 'written_reports', 'feature_matrix']
    request_algorithms = ['decision_tree', 'gaussian_processes', 'annealing', 'tree_of_parzen_estimators',
                          'light_gbm', 'random_search', 'adaboost', 'gradient_boosting', 'knn', 'random_forest',
                          'svm', 'xgboost', 'neural_network', 'regression', 'xgboost_gb',
                          'regularized_greedy_forest', 'k_nearest_neighbors', 'extra_trees', 'deep_neural_network',
                          'ml_algorithms_included']

    for system in systems:
        columns = [system.payment, system.programming_skills, system.datascience_skills, system.python, system.r,
                   system.java, system.scala, system.cloud_computing, system.linux, system.mac_os, system.windows,
                   system.automatic, system.numerical, system.time_series, system.images, system.videos, system.audios,
                   system.text, system.input_required, system.handling_missing_values,
                   system.outliers_detection_deletion, system.data_standardization, system.data_encoding,
                   system.feature_scaling, system.data_reduction, system.data_balancing, system.data_augmentation,
                   system.feature_generation, system.integrated_modeling, system.training,
                   system.anti_overfitting_approach,
                   system.evaluation_approach,
                   system.search, system.gui, system.hyperparameter_selection, system.metrics, system.charts,
                   system.web_service, system.online_model_training, system.preliminary_results, system.best_model,
                   system.evaluation, system.ensamble, system.leaderboard, system.model_characteristics,
                   system.written_reports, system.feature_matrix]
        ml_algorithms = [system.decision_tree, system.gaussian_processes, system.annealing,
                         system.tree_of_parzen_estimators, system.light_gbm, system.random_search, system.adaboost,
                         system.gradient_boosting, system.knn, system.random_forest, system.svm, system.xgboost,
                         system.neural_network, system.regression, system.xgboost_gb, system.regularized_greedy_forest,
                         system.k_nearest_neighbors, system.extra_trees, system.deep_neural_network,
                         system.ml_algorithms_included]
        i = 0

        # print("columns")

        for c in columns:
            if c is not None:
                # print(c)
                score[system] += (c and (user_info[request_columns[i]] is True))
            i += 1

        i = 0

        # print("ml_algorithms")
        for c in ml_algorithms:
            if c is not None:
                if user_info[request_algorithms[i]] is True:
                    # print(c)
                    score[system] += 0.1
            i += 1

    print("end of scoring systems")

    for i in range(len(request_columns)):
        if user_info[request_columns[i]] is True or user_info[request_columns[i]] is False:
            answercount += 1
            print(request_keys[i])
            print(user_info[request_keys[i]])
            print(answercount)

    for i in range(len(request_algorithms)):
        if user_info[request_algorithms[i]] is True or user_info[request_algorithms[i]] is False:
            answercount += 0.1
            print(request_keys[i])
            print(user_info[request_keys[i]])
            print(answercount)
        for system in systems:
            columns = [system.payment, system.programming_skills, system.datascience_skills, system.python, system.r,
                       system.java, system.scala, system.cloud_computing, system.linux, system.mac_os, system.windows,
                       system.automatic, system.numerical, system.time_series, system.images, system.videos,
                       system.audios,
                       system.text, system.input_required, system.handling_missing_values,
                       system.outliers_detection_deletion,
                       system.data_standardization, system.data_encoding, system.feature_scaling, system.data_reduction,
                       system.data_balancing, system.data_augmentation, system.feature_generation,
                       system.integrated_modeling,
                       system.training, system.decision_tree, system.gaussian_processes, system.annealing,
                       system.tree_of_parzen_estimators, system.light_gbm, system.random_search, system.adaboost,
                       system.gradient_boosting, system.knn, system.random_forest, system.svm, system.xgboost,
                       system.neural_network, system.regression, system.xgboost_gb, system.regularized_greedy_forest,
                       system.k_nearest_neighbors, system.extra_trees, system.deep_neural_network,
                       system.ml_algorithms_included, system.anti_overfitting_approach, system.evaluation_approach,
                       system.search, system.gui, system.hyperparameter_selection, system.metrics, system.charts,
                       system.web_service, system.online_model_training, system.preliminary_results, system.best_model,
                       system.evaluation, system.ensamble, system.leaderboard, system.model_characteristics,
                       system.written_reports, system.feature_matrix]
            for k in range(len(request_keys)):
                if crit_info[crit_keys[k]] is True and columns[k] is not None and user_info[request_keys[k]] != columns[
                    k]:
                    crit[system] = True

        # print(System.query.filter(System.name == 'User').all())
        results = []
        for s in sorted(score, key=score.get, reverse=True):
            if crit[s] is not True and s.name != 'User':
                results.append(s)

        result = ''
        print(answercount)
        for x in range(len(results)):
            print(score[results[x]])
            result += results[x].name + ':' + str(round(score[results[x]], 2)) + '=' + \
                      str(round((score[results[x]] / answercount) * 100, 2)) + '%|'
    return result


if __name__ == '__main__':
        app.run(debug=True, port=5001)
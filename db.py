from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AutoML.db'
db = SQLAlchemy(app)


class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)  # point system for final results
    crit = db.Column(db.Boolean)
    name = db.Column(db.String(50))

    programming_skills = db.Column(db.Boolean)  # Are Basic Programming skills required?
    datascience_skills = db.Column(db.Boolean)
    python = db.Column(db.Boolean)  # programming languages
    java = db.Column(db.Boolean)
    r = db.Column(db.Boolean)
    scala = db.Column(db.Boolean)
    payment = db.Column(db.Boolean)
    cloud_computing = db.Column(db.Boolean)
    linux = db.Column(db.Boolean)  # table for os?
    mac_os = db.Column(db.Boolean)
    windows = db.Column(db.Boolean)
    # automl = db.Cloumn(db.Boolean) answers are Yes or Texts

    # confusion_matrix = db.Column(db.Boolean)
    # runtime = db.Column(db.Integer)  # runtime rounded in min  #other possibility: 'runtime = db.Column(db.Float)'

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

s1 = System(name='Hyperopt-sklearn', programming_skills=True, python=True, r=True, java=True, scala=False,
            payment=False, cloud_computing=False, linux=True, windows=True,
            numerical=True, input_required='Train and test datasets.', handling_missing_values=False,
            outliers_detection_deletion=False, data_standardization=True, data_encoding=True,
            feature_scaling=True, data_reduction=True, data_balancing=True, integrated_modeling=True, training=True,
            decision_tree=True, gaussian_processes=True, annealing=True, tree_of_parzen_estimators=True, light_gbm=True,
            random_search=True, evaluation_approach=True, search='Model', gui=False, hyperparameter_selection=True,
            metrics=True, charts=False, web_service=False, preliminary_results=True, best_model=True, evaluation=True,
            automatic=False, ensamble=False)  # confusion_matrix=False, runtime=47,
s2 = System(name='Auto-sklearn', programming_skills=True, python=True, r=False, java=False, scala=False, payment=False,
            cloud_computing=False, linux=True,
            mac_os=False, windows=False, numerical=True, time_series=True, text=True,
            input_required='Train and test datasets.', handling_missing_values=True, data_standardization=True,
            data_encoding=True, feature_scaling=True, data_reduction=True, integrated_modeling=True, training=True,
            adaboost=True, decision_tree=True, gradient_boosting=True, knn=True, random_forest=True, svm=True,
            anti_overfitting_approach=True, evaluation_approach=True, search='Model', gui=False,
            hyperparameter_selection=True, metrics=True, charts=False, web_service=False, preliminary_results=False,
            ensamble=True, evaluation=True, automatic=False, best_model=False)
# confusion_matrix=False, runtime=120, productionize_model='Export model as a .pickle file.'
s3 = System(name='TPOT', programming_skills=True,
            python=True, r=False, java=False, scala=False, payment=False, cloud_computing=False, linux=True,
            mac_os=True, windows=True,
            numerical=True, time_series=False, images=True, text=True, handling_missing_values=True,
            outliers_detection_deletion=False, data_encoding=True, feature_scaling=True, data_reduction=True,
            data_balancing=False, integrated_modeling=True, training=True, adaboost=True,
            decision_tree=True, knn=True, logistic_regression=True, random_forest=True, svm=True, xgboost=True,
            anti_overfitting_approach=True, evaluation_approach=True, search='Population', gui=False,
            hyperparameter_selection=True, metrics=True, charts=False, web_service=False, preliminary_results=True,
            best_model=True, automatic=False, ensamble=False)  # confusion_matrix=False, runtime=69,
s4 = System(name='H2O AutoML', programming_skills=True, datascience_skills=True,
            python=True, java=False, scala=False, r=True, payment=False, cloud_computing=True, linux=True, mac_os=True,
            windows=True, ensamble=False,
            numerical=True, time_series=True, images=True, text=True, handling_missing_values=True,
            outliers_detection_deletion=False, data_standardization=True, data_encoding=True, data_balancing=True,
            integrated_modeling=True, training=True, neural_network=True, gradient_boosting=True, random_forest=True,
            xgboost=True, anti_overfitting_approach=True, search='Random search', gui=False,
            hyperparameter_selection=True, metrics=True, charts=False, web_service=False, preliminary_results=True,
            best_model=True, evaluation=True, model_characteristics=True, leaderboard=True, automatic=False)
#  confusion_matrix=False, runtime=53, productionize_model='Export model as POJO or MOJO format.'
s5 = System(name='SAS', programming_skills=False, datascience_skills=False, python=False, r=False, java=False,
            scala=False, cloud_computing=True, numerical=True, time_series=True, videos=False, audios=False, text=True,
            input_required='Whole dataset', handling_missing_values=True, outliers_detection_deletion=False,
            data_encoding=True, data_reduction=True, data_balancing=False, data_augmentation=True,
            integrated_modeling=True, training=True, neural_network=True, gradient_boosting=True, regression=True,
            random_forest=True, svm=True, anti_overfitting_approach=True, ensamble=False,
            evaluation_approach=True, search='Model', gui=False, hyperparameter_selection=True, metrics=True,
            charts=True, web_service=True, preliminary_results=False, best_model=True, evaluation=True,
            model_characteristics=True, leaderboard=True, automatic=False)  # confusion_matrix=False,
s6 = System(name='MLBox', programming_skills=True, datascience_skills=True, python=True, r=False, java=False,
            scala=False, cloud_computing=False, ensamble=False,
            payment=False, linux=True, mac_os=True, windows=True, numerical=True, videos=False, audios=False, text=True,
            input_required='Train and test datasets. Testset must not contain a target.',
            handling_missing_values=True, outliers_detection_deletion=False, data_encoding=True, data_reduction=False,
            integrated_modeling=True, training=True, random_forest=True, xgboost_gb=True, k_nearest_neighbors=True,
            logistic_regression=True, light_gbm=True, regularized_greedy_forest=True, extra_trees=True,
            evaluation_approach=True, search='Model', gui=False, hyperparameter_selection=True, metrics=True,
            charts=False, web_service=False, preliminary_results=True, best_model=True, evaluation=True,
            model_characteristics=True, automatic=False)  # confusion_matrix=False
s7 = System(name='Google AutoML', programming_skills=False, datascience_skills=False, python=False, r=False, java=False,
            scala=False, payment=True, cloud_computing=True,
            numerical=True, time_series=True, images=True, text=True, input_required='Whole dataset.',
            handling_missing_values=True, data_encoding=True, integrated_modeling=True, training=True,
            adaboost=True, gradient_boosting=True, gui=False, hyperparameter_selection=True,
            metrics=True, charts=True, web_service=True, ensamble=False,
            online_model_training=True, preliminary_results=True, best_model=True, evaluation=True,
            model_characteristics=True, automatic=False)
# confusion_matrix=True, runtime=60, productionize_model= 'Classification models are stored in the platform and can be
# loaded from there.'
s8 = System(name='Azure Machine Learning', programming_skills=True,
            python=True, r=False, java=False, scala=False, payment=True, cloud_computing=True,
            numerical=True, time_series=True, images=True, audios=True, text=True, ensamble=False,
            handling_missing_values=True, outliers_detection_deletion=True, data_standardization=True,
            data_encoding=True, feature_scaling=True, data_reduction=True, data_balancing=True, data_augmentation=True,
            feature_generation=True, training=True, decision_tree=True, logistic_regression=True, svm=True,
            evaluation_approach=True, search='Model', gui=True, metrics=True, charts=True, preliminary_results=True,
            best_model=True, evaluation=True, automatic=False, model_characteristics=True)
# confusion_matrix=True, runtime=50, productionize_model= 'Export model as a .pickle file.'
s9 = System(name='MLJar', programming_skills=False, datascience_skills=False,
            python=True, java=False, scala=False, r=True, payment=True, cloud_computing=True, numerical=True,
            time_series=True, text=True,
            input_required='Train and test datasets.', handling_missing_values=True, data_standardization=True,
            data_encoding=True, feature_scaling=True, feature_generation=True, integrated_modeling=True, training=True,
            deep_neural_network=True, gradient_boosting=True, k_nearest_neighbors=True, logistic_regression=True,
            random_forest=True, light_gbm=True, regularized_greedy_forest=True, extra_trees=True,
            anti_overfitting_approach=True, gui=True, hyperparameter_selection=True, metrics=True, charts=True,
            web_service=True, preliminary_results=True, ensamble=True, evaluation=True, automatic=False,
            best_model=False)
# confusion_matrix=False, runtime=77, productionize_model='Export model as .model files.'
s10 = System(name='ATM', programming_skills=True, datascience_skills=True,
             python=True, r=False, java=False, scala=False, payment=False, cloud_computing=False,
             linux=True, numerical=True, time_series=True, images=True, ensamble=False,
             videos=False, audios=False, text=False, input_required='Train and test datasets.', data_encoding=True,
             integrated_modeling=True, training=True, anti_overfitting_approach=True, gui=False,
             hyperparameter_selection=True, metrics=True, charts=False, web_service=True, preliminary_results=False,
             evaluation=True, model_characteristics=True, automatic=False,
             best_model=False)  # confusion_matrix=True,runtime=115
s11 = System(name='Auto_ml', programming_skills=True, datascience_skills=True, python=True, r=False, java=False,
             scala=False, cloud_computing=False, payment=False, windows=True, numerical=True,
             time_series=True, images=False, videos=False, audios=False, text=False, ensamble=False,
             input_required='Train and test datasets.', data_encoding=True, feature_scaling=True,
             feature_generation=True, integrated_modeling=True, training=True, gui=False, hyperparameter_selection=True,
             metrics=True, charts=False, web_service=False,
             preliminary_results=False, evaluation=True, model_characteristics=True, automatic=False, best_model=False)
# confusion_matrix=True, productionize_model='Export model as a .dill file.'
s12 = System(name='Amazon SageMaker ', programming_skills=False, datascience_skills=False, python=False, r=False,
             java=False, scala=False,
             payment=True, cloud_computing=True, numerical=True, input_required='Train and test datasets.',
             handling_missing_values=True, outliers_detection_deletion=True, data_standardization=True,
             data_encoding=True, feature_scaling=True, data_augmentation=True, integrated_modeling=True, training=True,
             anti_overfitting_approach=True, gui=False, hyperparameter_selection=True, metrics=True, charts=False,
             web_service=True, preliminary_results=True, ensamble=True, model_characteristics=True,
             automatic=False, best_model=False)
s13 = System(name='Uber Ludwig ', programming_skills=False, datascience_skills=True, ensamble=False,
             python=True, r=False, java=False, scala=False, cloud_computing=False, payment=False,
             linux=True, mac_os=True, numerical=True, time_series=True, images=True, audios=True, text=True,
             input_required='Train and test datasets.', handling_missing_values=True, data_standardization=True,
             data_encoding=True, feature_scaling=True, data_augmentation=False, integrated_modeling=True, training=True,
             anti_overfitting_approach=True, gui=False, hyperparameter_selection=True, metrics=True, charts=False,
             web_service=False, preliminary_results=False, model_characteristics=True, best_model=True, evaluation=True,
             automatic=False)
# productionize_model='Model is saved as a group of files, which can be loaded using a ludwig method.',
s14 = System(name='TransmogrifAI', python=False, r=False, java=False, scala=True, payment=False, cloud_computing=False,
             numerical=True, images=True, input_required='Whole dataset.', handling_missing_values=True,
             data_standardization=True, data_encoding=True, data_reduction=True, data_balancing=True,
             feature_generation=True, integrated_modeling=True, training=True, logistic_regression=True,
             random_forest=True, anti_overfitting_approach=True, gui=False, ensamble=False,
             hyperparameter_selection=True, metrics=True, charts=False, web_service=False, preliminary_results=False,
             model_characteristics=True, best_model=True, evaluation=True, automatic=False)
s15 = System(name='The Automatic Statistician', numerical=True, time_series=True, ensamble=False,
             handling_missing_values=True, data_encoding=True, data_reduction=True, data_balancing=True, training=True,
             hyperparameter_selection=True, web_service=False, written_reports=True, automatic=False,
             best_model=False, evaluation=False)
s16 = System(name='AutoKeras', programming_skills=True, datascience_skills=True,
             python=True, r=False, java=False, scala=False, payment=False, cloud_computing=False,
             linux=True, numerical=True, images=True, text=True, ensamble=False,
             input_required='Train and test datasets.', data_standardization=True, data_encoding=True,
             data_augmentation=True, integrated_modeling=True, training=True, gui=False, hyperparameter_selection=True,
             metrics=True, charts=False, web_service=False, preliminary_results=True, best_model=True, evaluation=True,
             automatic=False)
# confusion_matrix=False, runtime=61, productionize_model='Export model as a tf.keras.Model instance.'
s17 = System(name='Feature Tools', programming_skills=True, datascience_skills=True,
             python=True, r=False, java=False, scala=False, cloud_computing=False, payment=False,
             linux=True, mac_os=True, windows=True, numerical=True, time_series=True,
             input_required='Datasets and relations between them.', data_encoding=True, feature_generation=True,
             integrated_modeling=True, training=False, anti_overfitting_approach=False, ml_algorithms_included=False,
             evaluation_approach=False, search='None', gui=False, hyperparameter_selection=False, metrics=False,
             charts=False, web_service=False, online_model_training=False, preliminary_results=False,
             feature_matrix=True, automatic=False, best_model=False, ensamble=False,
             evaluation=False)  # productionize_model='Export features as .csv file.'
s18 = System(name='tsfresh', programming_skills=True, datascience_skills=True, ensamble=False,
             python=True, r=False, java=False, scala=False, cloud_computing=False, payment=False,
             linux=True, windows=True, numerical=False, time_series=True, images=False, videos=False,
             audios=False, text=False, input_required='Time series dataset and target dataset.',
             feature_generation=True, integrated_modeling=True, training=False, ml_algorithms_included=False,
             anti_overfitting_approach=False, evaluation_approach=False, search='None', gui=False,
             hyperparameter_selection=False, metrics=False, charts=False, web_service=False,
             online_model_training=False, preliminary_results=False, feature_matrix=True, automatic=False,
             best_model=False, evaluation=False)
user = System(name='User')

db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)
db.session.add(s5)
db.session.add(s6)
db.session.add(s7)
db.session.add(s8)
db.session.add(s9)
db.session.add(s10)
db.session.add(s11)
db.session.add(s12)
db.session.add(s13)
db.session.add(s14)
db.session.add(s15)
db.session.add(s16)
db.session.add(s17)
db.session.add(s18)
db.session.add(user)
db.session.commit()

systems = System.query.all()
test = ''
for system in systems:
    test = test + system.name + '|'
print(test)

# %% [markdown]
# # Proper AI/ML Workflow
#
# Run each cell one by one:
# 1. Import libraries
# 2. Load dataset
# 3. Check dataset
# 4. Clean data
# 5. Train model
# 6. Test accuracy

# %% [markdown]
# ## Step 1: Import libraries

# %%
import pandas as pd
from pathlib import Path

try:
    from IPython.display import display
except ImportError:
    display = print

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

print("Step 1 complete: libraries imported successfully.")

# %% [markdown]
# ## Step 2: Load dataset

# %%
project_root = Path.cwd()
if not (project_root / "dataset" / "Student Depression Dataset.csv").exists():
    project_root = Path("..").resolve()

DATASET_PATH = project_root / "dataset" / "Student Depression Dataset.csv"

df = pd.read_csv(DATASET_PATH)

print("Step 2 complete: dataset loaded successfully.")
print("Dataset shape:", df.shape)

# %% [markdown]
# ## Step 3: Check dataset

# %%
print("First 5 rows:")
display(df.head())

print("Data types:")
display(df.dtypes)

print("Missing values:")
display(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())

print("Target distribution:")
display(df["Depression"].value_counts())

# %% [markdown]
# ## Step 4: Clean data

# %%
X = df.drop(columns=["Depression", "id"])
y = df["Depression"]

categorical_columns = X.select_dtypes(include=["object", "str"]).columns.tolist()
numeric_columns = X.select_dtypes(exclude=["object", "str"]).columns.tolist()

numeric_transformer = SimpleImputer(strategy="median")

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_transformer, numeric_columns),
        ("categorical", categorical_transformer, categorical_columns),
    ]
)

print("Step 4 complete: cleaning pipeline created.")
print("Numeric columns:", numeric_columns)
print("Categorical columns:", categorical_columns)

# %% [markdown]
# ## Step 5: Train model

# %%
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                class_weight="balanced",
                n_jobs=-1,
            ),
        ),
    ]
)

model.fit(X_train, y_train)

print("Step 5 complete: model trained successfully.")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# %% [markdown]
# ## Step 6: Test accuracy

# %%
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Step 6 complete: model tested successfully.")
print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")

print("Confusion matrix:")
display(confusion_matrix(y_test, y_pred))

print("Classification report:")
print(classification_report(y_test, y_pred))

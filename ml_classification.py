import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

# 1. Create sample dataset (Emails and Labels)
emails = [
    "Congratulations! You won a free cruise text WIN to 55555",
    "Urgent account alert: Click here to claim your cash bonus now",
    "Hey, are we still meeting for lunch at 12:30 today?",
    "Please find attached the project updates and final presentation slides.",
    "Get cheap luxury watches, limited time discount offer!",
    "Hi Mom, I will be home late for dinner tonight, don't wait up.",
    "Investment opportunity! Double your money fast guaranteed risk free"
]
# 1 = Spam, 0 = Not Spam (Ham)
labels = [1, 1, 0, 0, 1, 0, 1]

# 2. Convert text data into numbers (Bag of Words)
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(emails)
y = np.array(labels)

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)

# 5. Make predictions on the test set
y_pred = clf.predict(X_test)

# 6. Evaluate model performance
print("--- Model Performance ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Not Spam", "Spam"]))

# 7. Predict on a completely new unseen email
new_email = ["Urgent! You won cash prizes! Click the link to claim."]
new_email_vectorized = vectorizer.transform(new_email)
prediction = clf.predict(new_email_vectorized)

result = "Spam" if prediction[0] == 1 else "Not Spam"
print("--- New Email Prediction ---")
print(f"Email: '{new_email[0]}'")
print(f"Prediction: {result}")

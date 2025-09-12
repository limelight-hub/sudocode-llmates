# **FEATURE EXTRACTION**
---
* sklearn.feature_extraction is used to convert data types such as text and images into numerical features that can be used by machine learning algorithms.
> **Feature Extraction**: convert raw data type (text, images) into numerical features

> **Feature Selection**: choose the best features

# **DictVectorizer**
---

Using **DictVectorizer** to convert a dictionary in Python into a matrix NumPy/SciPy that Scikit-learn can understand and process.
* Encoding Methods: DictVectorizer uses *one-hot* for categorical features.
* Sparsity: DictVectorizer uses *scipy.sparse matrix*


> **DictVectorizer** is only suitable with attribute fields (short text) rather than long text like content or title

> For long text (such as content, title), you can use TF-IDF **(TfidfVectorizer)**

# **Feature Hashing**
---
Class **FeatureHasher** is a high-speed, low-memory vectorizer that uses a technique known as feature hasing. FeatureHasher apply a hash function to the features to determine their column index in sample matrices directly.

* Pros: High-speed, using for large data.
* Cons: cannot inverse_transform

* title + content: tokenize to use for feature token counts
* source, topic, author: categorical (value = 1)
* picture_count, processed: numerical features

# **TEXT FEATURE EXTRACTION**
---
Text Analysis is a major application field for machine learning algorithms.

scikit-learn provides many ways to extract numerical features from text content:
* **tokenizing**: strings and giving an integer id for each possible token, for instance by using white-spaces, and punctuation as token separators.
* **counting**: the occurrences of tokens in each document.
* **normalizing** and weighting with diminishing importance tokens that occur in the majority of documents

> **Bag of Words (Bag of n-grams)**: tokenization + counting + normalization

## **Bag of Words**
> Using **CountVectorizer** to tokenize text and build vocabulary, return a sparse matrix with occurrence frequency

* each individual token occurrence frequency (normalized or not) is treated as a feature
* the vector of all the token frequencies for a given document is considered a multivariate sample.

## **TF-IDF**
* CountVectorizer only returns occurrence frequency of word.
* Using **TfidfTransformer** or **TfidfVectorizer** to scale, reduct weight of common words + increase weight of rare words.

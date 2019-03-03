{
    "nbformat_minor": 1, 
    "cells": [
        {
            "execution_count": 1, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [
                {
                    "output_type": "stream", 
                    "name": "stdout", 
                    "text": "Collecting graphviz\n  Downloading https://files.pythonhosted.org/packages/1f/e2/ef2581b5b86625657afd32030f90cf2717456c1d2b711ba074bf007c0f1a/graphviz-0.10.1-py2.py3-none-any.whl\nInstalling collected packages: graphviz\nSuccessfully installed graphviz-0.10.1\n"
                }
            ], 
            "source": "#install graphviz for tree visualization\n!pip install graphviz"
        }, 
        {
            "execution_count": 2, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": "#import required libraries\nfrom sklearn.tree import DecisionTreeClassifier \nfrom sklearn import tree \nfrom sklearn.preprocessing import LabelEncoder \nfrom sklearn.tree import export_graphviz\nfrom graphviz import Source\nfrom IPython.display import SVG\nimport pandas as pd \nimport numpy as np \nimport io\nimport requests"
        }, 
        {
            "execution_count": 4, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [
                {
                    "output_type": "stream", 
                    "name": "stdout", 
                    "text": "   Practice Abid_Dietary IsMotivated IsFit\n0  Moderate          Yes         Yes   Yes\n1      good           No         Yes   Yes\n2        No           No         Yes    No\n3  Moderate           No          No    No\n4  Moderate           No         Yes   Yes\n5  Moderate           No         Yes   Yes\n6        No          Yes          No    No\n7      good          Yes          No    No\n"
                }
            ], 
            "source": "#Read training Dataset \nurl=\"https://raw.githubusercontent.com/IBMRedbooks/AI_Analyst/master/PlayerFitness.csv\"\ndf=pd.read_csv(url)\nprint(df)"
        }, 
        {
            "execution_count": 5, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [
                {
                    "output_type": "stream", 
                    "name": "stdout", 
                    "text": "Features in numeric form\n   Practice_  Abid_Dietary_  IsMotivated_\n0          0              1             1\n1          2              0             1\n2          1              0             1\n3          0              0             0\n4          0              0             1\n5          0              0             1\n6          1              1             0\n7          2              1             0\n*********************************************\nLabel in numeric form\n0    1\n1    1\n2    0\n3    0\n4    1\n5    1\n6    0\n7    0\nName: IsFit_, dtype: int64\nThe prediction result for test case, given features are: practice is moderate, Abid_Dietary is yes and  IsMotivated is yes\n[1]\n"
                }
            ], 
            "source": "# Transform the dataset into numeric form to enable it to fit in the tree algorithm\n#For instance, value Yes=1 and value No=0\n#This applies for the columns such as IsFit, isMotivated and Abid Dietary.\n#As for the column \"practice\"  the values are Moderate =0, No=1, Good=2\nlb = LabelEncoder() \ndf['Practice_'] = lb.fit_transform(df['Practice']) \ndf['Abid_Dietary_'] = lb.fit_transform(df['Abid_Dietary'] ) \ndf['IsMotivated_'] = lb.fit_transform(df['IsMotivated'] )  \ndf['IsFit_'] = lb.fit_transform(df['IsFit'] ) \nX = df.iloc[:,4:7] \nY = df.iloc[:,7]\nprint(\"Features in numeric form\")\nprint(X)\nprint(\"*********************************************\")\nprint(\"Label in numeric form\")\nprint(Y)\n# Prepare a testcase\nX_test=[[0 for x in range(3)] for y in range(1)]\nX_test[0][0]=2\nX_test[0][1]=1\nX_test[0][2]=1\n#Train a Decision tree\nd_tree = DecisionTreeClassifier(criterion='entropy')\nd_tree.fit(X.astype(int), Y.astype(int))\n#Test using sample test X_test\ny_pred_en = d_tree.predict(X_test)\n#The prediction for X-test\nprint(\"The prediction result for test case, given features are: practice is moderate, Abid_Dietary is yes and  IsMotivated is yes\")\nprint(y_pred_en)\n\n"
        }, 
        {
            "execution_count": 6, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [
                {
                    "execution_count": 6, 
                    "metadata": {}, 
                    "data": {
                        "text/plain": "<IPython.core.display.SVG object>", 
                        "image/svg+xml": "<svg height=\"373pt\" viewBox=\"0.00 0.00 407.00 373.00\" width=\"407pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n<g class=\"graph\" id=\"graph0\" transform=\"scale(1 1) rotate(0) translate(4 369)\">\n<title>Tree</title>\n<polygon fill=\"#ffffff\" points=\"-4,4 -4,-369 403,-369 403,4 -4,4\" stroke=\"transparent\"/>\n<!-- 0 -->\n<g class=\"node\" id=\"node1\">\n<title>0</title>\n<polygon fill=\"none\" points=\"211,-365 49,-365 49,-297 211,-297 211,-365\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"130\" y=\"-349.8\">IsMotivated_ &lt;= 0.5</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"130\" y=\"-334.8\">entropy = 1.0</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"130\" y=\"-319.8\">samples = 8</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"130\" y=\"-304.8\">value = [4, 4]</text>\n</g>\n<!-- 1 -->\n<g class=\"node\" id=\"node2\">\n<title>1</title>\n<polygon fill=\"none\" points=\"116,-253.5 0,-253.5 0,-200.5 116,-200.5 116,-253.5\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"58\" y=\"-238.3\">entropy = 0.0</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"58\" y=\"-223.3\">samples = 3</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"58\" y=\"-208.3\">value = [3, 0]</text>\n</g>\n<!-- 0&#45;&gt;1 -->\n<g class=\"edge\" id=\"edge1\">\n<title>0-&gt;1</title>\n<path d=\"M106.4245,-296.9465C98.6463,-285.7113 89.9861,-273.2021 82.1645,-261.9043\" fill=\"none\" stroke=\"#000000\"/>\n<polygon fill=\"#000000\" points=\"84.9452,-259.7719 76.3753,-253.5422 79.1898,-263.7564 84.9452,-259.7719\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"71.9032\" y=\"-274.4389\">True</text>\n</g>\n<!-- 2 -->\n<g class=\"node\" id=\"node3\">\n<title>2</title>\n<polygon fill=\"none\" points=\"270,-261 134,-261 134,-193 270,-193 270,-261\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"202\" y=\"-245.8\">Practice_ &lt;= 0.5</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"202\" y=\"-230.8\">entropy = 0.722</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"202\" y=\"-215.8\">samples = 5</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"202\" y=\"-200.8\">value = [1, 4]</text>\n</g>\n<!-- 0&#45;&gt;2 -->\n<g class=\"edge\" id=\"edge2\">\n<title>0-&gt;2</title>\n<path d=\"M153.5755,-296.9465C159.6671,-288.1475 166.2996,-278.5672 172.6466,-269.3993\" fill=\"none\" stroke=\"#000000\"/>\n<polygon fill=\"#000000\" points=\"175.5571,-271.3442 178.3715,-261.13 169.8017,-267.3597 175.5571,-271.3442\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"182.8437\" y=\"-282.0267\">False</text>\n</g>\n<!-- 3 -->\n<g class=\"node\" id=\"node4\">\n<title>3</title>\n<polygon fill=\"none\" points=\"188,-149.5 72,-149.5 72,-96.5 188,-96.5 188,-149.5\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"130\" y=\"-134.3\">entropy = 0.0</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"130\" y=\"-119.3\">samples = 3</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"130\" y=\"-104.3\">value = [0, 3]</text>\n</g>\n<!-- 2&#45;&gt;3 -->\n<g class=\"edge\" id=\"edge3\">\n<title>2-&gt;3</title>\n<path d=\"M178.4245,-192.9465C170.6463,-181.7113 161.9861,-169.2021 154.1645,-157.9043\" fill=\"none\" stroke=\"#000000\"/>\n<polygon fill=\"#000000\" points=\"156.9452,-155.7719 148.3753,-149.5422 151.1898,-159.7564 156.9452,-155.7719\" stroke=\"#000000\"/>\n</g>\n<!-- 4 -->\n<g class=\"node\" id=\"node5\">\n<title>4</title>\n<polygon fill=\"none\" points=\"342,-157 206,-157 206,-89 342,-89 342,-157\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"274\" y=\"-141.8\">Practice_ &lt;= 1.5</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"274\" y=\"-126.8\">entropy = 1.0</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"274\" y=\"-111.8\">samples = 2</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"274\" y=\"-96.8\">value = [1, 1]</text>\n</g>\n<!-- 2&#45;&gt;4 -->\n<g class=\"edge\" id=\"edge4\">\n<title>2-&gt;4</title>\n<path d=\"M225.5755,-192.9465C231.6671,-184.1475 238.2996,-174.5672 244.6466,-165.3993\" fill=\"none\" stroke=\"#000000\"/>\n<polygon fill=\"#000000\" points=\"247.5571,-167.3442 250.3715,-157.13 241.8017,-163.3597 247.5571,-167.3442\" stroke=\"#000000\"/>\n</g>\n<!-- 5 -->\n<g class=\"node\" id=\"node6\">\n<title>5</title>\n<polygon fill=\"none\" points=\"265,-53 149,-53 149,0 265,0 265,-53\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"207\" y=\"-37.8\">entropy = 0.0</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"207\" y=\"-22.8\">samples = 1</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"207\" y=\"-7.8\">value = [1, 0]</text>\n</g>\n<!-- 4&#45;&gt;5 -->\n<g class=\"edge\" id=\"edge5\">\n<title>4-&gt;5</title>\n<path d=\"M250.3783,-88.9777C244.2113,-80.0954 237.5539,-70.5067 231.3499,-61.5711\" fill=\"none\" stroke=\"#000000\"/>\n<polygon fill=\"#000000\" points=\"234.1497,-59.4666 225.5715,-53.2485 228.3997,-63.4589 234.1497,-59.4666\" stroke=\"#000000\"/>\n</g>\n<!-- 6 -->\n<g class=\"node\" id=\"node7\">\n<title>6</title>\n<polygon fill=\"none\" points=\"399,-53 283,-53 283,0 399,0 399,-53\" stroke=\"#000000\"/>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"341\" y=\"-37.8\">entropy = 0.0</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"341\" y=\"-22.8\">samples = 1</text>\n<text fill=\"#000000\" font-family=\"Times,serif\" font-size=\"14.00\" text-anchor=\"middle\" x=\"341\" y=\"-7.8\">value = [0, 1]</text>\n</g>\n<!-- 4&#45;&gt;6 -->\n<g class=\"edge\" id=\"edge6\">\n<title>4-&gt;6</title>\n<path d=\"M297.6217,-88.9777C303.7887,-80.0954 310.4461,-70.5067 316.6501,-61.5711\" fill=\"none\" stroke=\"#000000\"/>\n<polygon fill=\"#000000\" points=\"319.6003,-63.4589 322.4285,-53.2485 313.8503,-59.4666 319.6003,-63.4589\" stroke=\"#000000\"/>\n</g>\n</g>\n</svg>"
                    }, 
                    "output_type": "execute_result"
                }
            ], 
            "source": "#Visualize the decision tree\ngraph = Source(export_graphviz(d_tree, out_file=None, feature_names=X.columns))\nSVG(graph.pipe(format='svg'))"
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }
    ], 
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3.5", 
            "name": "python3", 
            "language": "python"
        }, 
        "language_info": {
            "mimetype": "text/x-python", 
            "nbconvert_exporter": "python", 
            "version": "3.5.5", 
            "name": "python", 
            "file_extension": ".py", 
            "pygments_lexer": "ipython3", 
            "codemirror_mode": {
                "version": 3, 
                "name": "ipython"
            }
        }
    }, 
    "nbformat": 4
}
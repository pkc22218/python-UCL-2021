"""grep - a simple search engine
"""
"""
Description: a simple search engine which builds indexes for a given set of files on your computer
(a) Functioncommon_elements(lis_1,lis_2): lis_1, lis_2 are simple one-dimensional lists. This function returns 
a list which contains the elements common to both lists. 

(b) Functionbuild_index(file_list,index,title_index) In this function you will use the list of file names in 
the variable file_list. You will create two indexes index and title_index which are both dictionaries. 

(c) Functionsearch(index,query): search() function which searches your index. The parameter query is a string
containing the words to search for. 

"""
import os, string

def common_elements(lis1, lis2):
    """Find the common elements in two lists.

    Args:
        lis1 (list): one of the lists to compare
        lis2 (list): the other list to compare

    Returns:
        list : contains the elements common to both lists.
    """    
    set_lis1 = set(lis1)
    set_lis2 = set(lis2)
    common = set_lis1.intersection(set_lis2)
    common_list = []
    for word in common:
        common_list.append(word)
    return common_list


def build_index(file_list, index, title_index):
    """Build a word index and a title index for all the files in a file list.

    Args:
        file_list (list): List containing file names
        index (dictionary): Index mapping words to filenames
        title_index (dictionary): Index mapping filenames to the title of the article.
    """
    for file in file_list:
        with open(file,"r") as file_input:
            content_list = file_input.read().lower().split()
            for word in range(len(content_list)):
                content_list[word] = content_list[word].strip(string.punctuation)
            content = []
            for word in content_list:
                if word not in content:
                    content.append(word)                 
            for word in content:
                if word not in index:
                    index[word] = []
                index[word].append(file)
        file_input.close
        with open(file,"r") as file_input:
            title = file_input.readline().rstrip()
            title_index[file] = title
        file_input.close
    
    return content



def search(index, query):
    """Search the index for the words in the query string.

    Args:
        index (dictionary): dictionary containing word to filename mapping.
        query (string): string containing words in the query. String is lowercase.

    Returns:
        list: list of file in which all the words in the query appear.
    """   
    query_list = query.lower().split()
    
    last_file = []
    for i in range(len(query_list)):
        current_file = []
        if query_list[i] in index:
            current_file += index[query_list[i]]
        else:
            current_file = []
        if i > 0:
            current_file = common_elements(current_file,last_file)
        last_file = current_file
    return current_file


def pretty_print(index, title_index):
    """Print the dictionaries passed as parameters

    Args:
        index (dictionary): Index mapping words to filenames
        title_index (dictionary): Index mapping filenames to the title of the article.
    """    
    print("\nIndex:")
    print(index)
    print("\nFile names and titles:")
    print(title_index)


def get_filenames(directory_name):
    """Return list of the files in the given directory.

    Args:
        directory_name (directory): Name of the directory

    Returns:
        list: list of filenames in the directory
    """    
    file_list = []

    for filename in os.listdir(directory_name):
        if filename.endswith('.txt'):
            file_list.append(os.path.join(directory_name, filename))

    return file_list


def menu(index, titles):
    """Menu for the application

    Args:
        index (dictionary): Index mapping words to filenames
        title_index (dictionary): Index mapping filenames to the title of the article.
    """    
    search_query = input('Enter a search query, (empty to finish): ')    

    while search_query != '':
        filename_list = search(index, search_query)
        print("Results: ", search_query)
        if len(filename_list) == 0:
            print("No results")
        else:
            for file in filename_list:
                title = titles[file]
                print("File: ", file, "Title: ", title)
        search_query = input('Enter a search query, (empty to finish): ')


def main():
    
    # Test 1: test common_elements
    # print(common_elements(['a', 'b', 'c'], ['a', 'p', 'c']))
    # print(common_elements(['a', 'b', 'c'],['x', 'y', 'z']))
    # print(common_elements(['a', 'b', 'a'],['a', 'a', 'a']))  

    # Test 2: test with small files
    index = {}
    titles = {}
    build_index(['200.txt'], index, titles)
    pretty_print(index, titles)

    # Test 3: test with bbc sport news files
    #index = {}
    #titles = {}    
    #build_index(get_filenames('bbc_football'), index, titles)
    #pretty_print(index, titles)

    # Test 4: test with small files
    #index = {}
    #titles = {}
    #build_index(['200.txt'], index, titles)
    #print(index)
    #print("\n: ", search(index, 'real madrid'))
    #print("\ncoltrane: ", search(index, 'coltrane'))
    #print('\nellington: ', search(index, 'ellington'))
    #print('\nsentimental journey: ', search(index, 'sentimental journey'))
    #print('\nnot_in_files', search(index, 'not_in_files'))
    #print('\nlong journey', search(index, 'long journey'))

    # Test 5:test all
    #index = {}
    #titles = {} 
    #build_index(get_filenames('bbc_football'), index, titles)
    #menu(index, titles)


if __name__ == '__main__':

    main()


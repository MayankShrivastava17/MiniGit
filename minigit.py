import os
import hashlib
import json

class MiniGit:
    def __init__(self, repo_dir=".minigit"):
        """
        Initialize the MiniGit class and repository directory.
        If the repository directory doesn't exist, it's created along with the objects directory.
        """
        self.repo_dir = repo_dir
        self.objects_dir = os.path.join(self.repo_dir, "objects")
        self.index_file = os.path.join(self.repo_dir, "index")
        
        if not os.path.exists(self.repo_dir):
            os.makedirs(self.repo_dir)
            os.makedirs(self.objects_dir)
            self._write_index({})  # Initialize an empty index
        
        print(f"Initialized empty MiniGit repository in {self.repo_dir}")

    def _hash_object(self, data):
        """
        Create a SHA-1 hash of the input data.
        This simulates how Git hashes the content of files and commits.
        """
        return hashlib.sha1(data.encode()).hexdigest()

    def _write_index(self, index_data):
        """
        Write the current state of the index (staging area) to the index file in JSON format.
        """
        with open(self.index_file, 'w') as f:
            json.dump(index_data, f)

    def _read_index(self):
        """
        Read and return the current state of the index.
        If no index exists, return an empty dictionary.
        """
        if os.path.exists(self.index_file):
            with open(self.index_file, 'r') as f:
                return json.load(f)
        return {}

    def init(self):
        """
        Initialize the repository. If already initialized, notify the user.
        """
        if os.path.exists(self.repo_dir):
            print("Repository already initialized.")
        else:
            os.makedirs(self.repo_dir)
            os.makedirs(self.objects_dir)
            self._write_index({})
            print(f"Initialized empty MiniGit repository in {self.repo_dir}")

    def add(self, file_path):
        """
        Add a file to the index (staging area) by hashing its content and storing it in the objects directory.
        """
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return

        with open(file_path, 'r') as f:
            content = f.read()
        
        # Hash the content
        file_hash = self._hash_object(content)

        # Store the object in the objects directory
        object_file = os.path.join(self.objects_dir, file_hash)
        with open(object_file, 'w') as f:
            f.write(content)
        
        # Add the file to the index
        index = self._read_index()
        index[file_path] = file_hash
        self._write_index(index)
        
        print(f"Added file {file_path} to the index.")

    def commit(self, message):
        """
        Commit the current state of the index with a commit message.
        The commit is stored in the objects directory as a snapshot.
        """
        index = self._read_index()
        if not index:
            print("No changes to commit.")
            return

        # Create commit object
        commit = {
            'message': message,
            'files': index
        }
        commit_data = json.dumps(commit, indent=4)
        commit_hash = self._hash_object(commit_data)

        # Save the commit to objects
        commit_file = os.path.join(self.objects_dir, commit_hash)
        with open(commit_file, 'w') as f:
            f.write(commit_data)
        
        print(f"Committed with message: {message}")
        print(f"Commit hash: {commit_hash}")

'''
# Example usage of MiniGit
if __name__ == "__main__":
    repo = MiniGit()
    repo.init()  # Initialize repository
    repo.add("test.txt")  # Add file to index
    repo.commit("Initial commit")  # Commit changes
  '''

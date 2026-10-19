from models import init_db
from sample_model import SampleModel
def main():
    session = init_db()
    # Add a test entry
    new_sample = SampleModel()
    session.add(new_sample)
    session.commit()
    print('Sample model created and initialized successfully.')

if __name__ == '__main__':
    main()
from bs4 import BeautifulSoup
import pandas as pd
from itertools import islice
import time


def text2csv(fin, fout, has_score=True):
    columns = ['id', 'score', 'text', 'summary']
    df = pd.DataFrame(columns=columns)
    n = 9 if has_score else 8
    with open(fin, encoding='utf8') as f:
        while True:
            text = ''.join(islice(f, n))
            if not text:
                break
            sp = BeautifulSoup(text, 'html.parser')
            dt = {
                'id': sp.doc['id'],
                'text': sp.doc.short_text.get_text().strip(),
                'score': sp.doc.human_label.get_text() if has_score else '',
                'summary': sp.doc.summary.get_text().strip()
            }
            df = df.append(dt, ignore_index=True)
    df.to_csv(fout, index=False)

def part_I2csv():
    pass



def gen_csv():
    tik = time.time()
    fin = '../data/LCSTS_ORIGIN/DATA/PART_III.txt'
    fout = '../data/LCSTS_csv/part3.csv'
    text2csv(fin, fout)
    tok = time.time()
    print(f'{tok - tik:.3f} sec')
    fin = '../data/LCSTS_ORIGIN/DATA/PART_II.txt'
    fout = '../data/LCSTS_csv/part2.csv'
    text2csv(fin, fout)
    tok2 = time.time()
    print(f'{tok2 - tok:.3f} sec')


if __name__ == '__main__':
    fp='../data/LCSTS_ORIGIN/DATA/PART_I.txt'
    columns = ['id', 'score', 'text', 'summary']
    df = pd.DataFrame(columns=columns)
    with open(fp, encoding='utf8') as f:
        sp = BeautifulSoup(f.read(), 'html.parser')
    pass


import FileTree from './FileTree/FileTree';
import RepoEntry from './RepoEntry/RepoEntry';
import styles from './RepoTree.module.css';
import type { RepoNode } from '@/types/repo';

const mockNodes: RepoNode[] = [
    { type: 'file', name: 'README.md', path: 'README.md' },
    { type: 'file', name: 'package.json', path: 'package.json' },
    {
        type: 'folder',
        name: 'src',
        children: [
            { type: 'file', name: 'index.ts', path: 'src/index.ts' },
            { type: 'file', name: 'App.tsx', path: 'src/App.tsx' },
            {
                type: 'folder',
                name: 'components',
                children: [
                    { type: 'file', name: 'Button.tsx', path: 'src/components/Button.tsx' },
                ],
            },
        ],
    },
    {
        type: 'folder',
        name: 'public',
        children: [
            { type: 'file', name: 'favicon.ico', path: 'public/favicon.ico' },
        ],
    },
];

export default function RepoTree() {
    return (
    <div className={styles.repoTree}>
        <RepoEntry />
        <FileTree nodes={mockNodes} />
    </div>
    );
}


const AuthButton = ({ children }) => {
    return (
        <button type="submit" className="block w-full bg-indigo-400 rounded-lg p-2 text-white text-lg font-medium hover:cursor-pointer">
            {children}
        </button>
    )
}

export default AuthButton